from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        """
        allauth를 통해서 유저를 저장할 때 호출됩니다. 유저 객체에 추가적인 정보를 담기 위해서 오버라이드를 실시했습니다.
        """
        user = super(SocialAccountAdapter, self).save_user(request, sociallogin, form)


