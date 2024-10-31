import os

from pages.transferOnePage import transferPage
from sites.sites import bwiki, wikigg

def transferPage(oldSite: Site, newSite: Site, pageName: str, username: str, password: str, sessiondata: str):
    # 登录到旧站点
    oldSite.login(username, password)
    
    # 登录到新站点
    newSite.login(sessiondata=sessiondata)
    
    # 检查页面是否存在于旧站点
    if not oldSite.pages[pageName].exists:
        print(f"页面 {pageName} 在旧站点不存在，跳过")
        return

    # 获取页面的命名空间编号
    namespace = oldSite.pages[pageName].namespace
    
    # 检查是否为模板页面（命名空间编号为10）
    if namespace.id != 10:
        print(f"页面 {pageName} 不是模板页面，跳过")
        return

    # 获取旧站点页面的文本内容
    oldpage_text = oldSite.pages[pageName].text
    
    # 获取新站点页面的文本内容
    newpage = newSite.pages[pageName]
    newpage_text = newpage.text if newpage.exists else ""
    
    # 检查内容是否不同
    if oldpage_text != newpage_text:
        # 同步页面内容
        newpage.edit(oldpage_text, summary=f"同步模板页面 {pageName}")
        print(f"页面 {pageName} 已同步")
    else:
        print(f"页面 {pageName} 内容相同，无需同步")

# 示例使用
if __name__ == '__main__':
    wikigg_user_name = 'your_wikigg_username'
    wikigg_user_password = 'your_wikigg_password'
    bwiki_session_data = 'your_bwiki_session_data'
    pageName = '火花弹'
    
    transferPage(oldSite=wikigg, newSite=bwiki, pageName=pageName, username=wikigg_user_name, password=wikigg_user_password, sessiondata=bwiki_session_data)
