from django import forms
from .models import Question, Choice

class VoteForm(forms.Form):
    # fieldを追加する: 空欄のまま送信してもOK
    new_option = forms.CharField(max_length=200, required=False)
    
    def __init__(self, *args, **kwargs):
        # やっていることの意図はなんとなくわかるが、superの詳細は理解できなかった
        self.question = kwargs.pop('question')
        super(VoteForm, self).__init__(*args, **kwargs)
        CHOICES = [(ch.id, ch.choice_text) for ch in self.question.choice_set.all()]
        # IDは仮の値として-1とした
        CHOICES.append((-1, 'other option (please specify in the box below)'))
        # widgetsとしてforms.radioselectにするとラジオボタンに。（デフォルトはプルダウン）
        self.fields['your_choice'] = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    
    def clean_your_choice(self):
        your_choice = self.cleaned_data.get('your_choice')
        return int(your_choice)

    def clean(self):
        '''フォーム全体に対するチェック処理'''
        cleaned_data = super(VoteForm, self).clean()
        choice_id = self.cleaned_data.get('your_choice')
        new_option = self.cleaned_data.get('new_option')
        if choice_id < 0:
            if not new_option:
                raise forms.ValidationError(
                    'Please specify a new option (or choose an existing one)!'
                )
        else:
            if new_option:
                raise forms.ValidationError(
                    'Do not specify a new option with also choosing an existing one!'
                )
    
    def save(self):
        # Valid後の綺麗なデータ
        choice_id = self.cleaned_data.get('your_choice')
        
        # 新しく選択されたidだった場合
        if choice_id < 0:
            new_option = Choice(
                question=self.question,
                choice_text=self.cleaned_data.get('new_option'),
                votes=1
            )
            new_option.save()
        else:
            # 選択された選択肢を取得
            selected_choice = Choice.objects.get(pk=choice_id)
            selected_choice.votes += 1
            selected_choice.save()