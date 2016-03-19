# -*- coding:utf-8 -*-
from datetime import datetime
from database import db

'''
此檔案為通用的類別，例如繼承用，地區，貨幣等等查詢為主的 model
'''

class SystemInfo(db.Model):
    # 抽象 model，作為共通繼承欄位用
    __abstract__ = True

    # auto_now_add => 新增資料時為 true，表示自動加時間
    # utc 會自動抓 協調世界時間，如果要抓區域時間請改用 now
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    # blank 試驗證實的判斷表示可為空，null 是 datebase的判斷，表示可 null
    delete_time = db.Column(db.DateTime, nullable=True)
    # 是否被刪除的註記
    deleted_tag = db.Column(db.Boolean, default=True)
    # 操作的身份，可能是管理者或使用者或系統身份
    oeperate_account = db.Column(db.String(40), nullable=True)

    def __repr__(self):
        print "<SystemInfo: create_time:'%s', update_time='%s', delete_time='%s', deleted_tag='%r', oeperate_account='%s'>" % (
            self.create_time,
            self.update_time,
            self.delete_time,
            self.deleted_tag,
            self.oeperate_account
        )