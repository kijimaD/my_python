"""通知のテスト"""

from plyer import notification

notification.notify(
    title='通知だよ',
    message='これはメッセージだよ',
    app_name='アプリ名だよ',
#    app_icon='./icon.jpg'
)
