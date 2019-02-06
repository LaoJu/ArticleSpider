# -*- coding: utf-8 -*-
# @File  : zhihu_login.py
# @Author: LaoJu
# @Date  : 2019/2/6
# @Desc  :

import requests

headers = {
    # 'accept':'*/*',
    # 'accept-encoding':'gzip, deflate, br',
    # 'accept-language':'zh-CN,zh;q=0.9',
    # 'cache-control':'no-cache',
    # 'content-length':'0',
    'cookie':'tgw_l7_route=4860b599c6644634a0abcd4d10d37251; _zap=0aab3c20-6b1b-49cb-8dbc-4f7973e6aab9; _xsrf=49e7f75f-286f-48b9-8e72-2da10017c358; d_c0="AOCjTp3Y8A6PTnKngoIJp0Wqgg4EbzsDdxQ=|1549461080"; capsion_ticket="2|1:0|10:1549461257|14:capsion_ticket|44:MTExODIzZjYwZDBkNDI2OTk4NDkxMTc4NjJmMWUyZTU=|be113653224091e1de5e51554e9c96041195c4d6a63c02f2b3a5af8d3d44b975"',
    # 'origin':'https://www.zhihu.com',
    # 'pragma':'no-cache',
    # 'referer':'https://www.zhihu.com/signup?next=%2F',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'x-ab-param':'li_gbdt=default;top_newfollowans=0;top_quality=0;top_ydyq=X;tp_discussion_feed_type_android=2;tp_header_style=0;se_click2=0;se_second_search=0;se_websearch=3;top_reason=1;top_test_4_liguangyi=1;tp_dis_version=0;zr_ans_rec=gbrank;se_mfq=0;se_search_feed=N;top_newfollow=0;top_thank=1;se_spb309=0;se_webrs=0;top_billpic=0;top_recall_deep_user=1;top_root=0;top_sess_diversity=-1;se_km_ad_locate=0;top_30=0;top_cc_at=1;gw_guide=0;pin_efs=orig;se_billboardsearch=0;se_consulting_price=n;top_recall_exp_v2=1;top_vidnocon=0;zr_article_rec_rank=truncate;li_album_liutongab=0;se_ios_spb309bugfix=0;top_round_table=0;top_core_session=-1;top_distinction=0;top_question_ask=1;top_source=0;se_ad_index=10;se_qanchor=0;se_zu_onebox=0;se_major_onebox=major;top_hkc_test=1;top_sj=2;tp_answer_meta_guide=1;se_entity=on;soc_zero_follow=0;top_bill=0;zr_rel_search=base;se_daxuechuisou=new;se_new_suggest=0;top_billab=0;se_majorob_style=0;top_root_ac=1;top_video_rerank=-1;qa_video_answer_list=0;se_backsearch=0;top_follow_reason=0;top_promo=1;tp_m_intro_re_topic=0;tp_sft=a;ug_follow_answerer=0;ls_new_video=0;se_correct_ab=0;top_nucc=0;zr_infinity=zr_infinity_close;pf_newguide_vertical=1;se_webmajorob=0;se_zu_recommend=0;soc_icon=1;top_nad=1;top_rank=0;zr_video_rec=zr_video_rec:base;se_time_search=new;top_user_gift=0;pin_ef=orig;se_new_market_search=on;top_freecontent=1;top_gif=0;top_v_album=1;zr_km_feed_rpm=default;li_lt_tp_score=1;qa_test=0;top_new_feed=1;top_yc=0;top_new_user_gift=0;tp_related_tps_movie=a;se_auto_syn=0;se_topicseed=0;top_billupdate1=2;top_new_user_rec=0;top_ntr=1;tp_sticky_android=0;ug_zero_follow=0;se_premium_member=0;se_prf=0;se_wannasearch=0;top_card=-1;top_hotlist=1;top_raf=y;top_rerank_reformat=-1;se_likebutton=0;se_wiki_box=1;top_feedre=1;tp_related_topics= a;tp_write_pin_guide=3;zr_boost_recall=0;se_colos=1;se_webtimebox=0;soc_bigone=0;qa_answerlist_ad=0;top_brand=1;top_is_gr=0;top_recall_exp_v1=1;top_universalebook=1;top_billvideo=0;top_tagextend=1;se_expired_ob=0;se_sensitive=0;soc_brandquestion=1;top_yhgc=0;qa_web_answerlist_ad=0;se_config=1;se_consulting_switch=off;soc_special=0;tp_qa_metacard_top=0;zr_art_rec_rank=base;zr_km_material_buy=2;top_native_answer=1;top_wonderful=1;tp_qa_metacard=1;li_filter_ttl=1;li_ts_sample=old;pf_creator_card=1;se_ios_spb309=0;se_minor_onebox=d;se_preset_tech=0;se_p_slideshow=0;top_ebook=0;top_newuser_feed=0;tp_discussion_feed_card_type=2;se_roundtable=0;top_creator_level=0;top_followtop=1;top_login_card=1;top_tr=0;zr_art_rec=base',
    # 'x-requested-with':'fetch',
    # 'x-udid':'AGDCCYS9QwuPTuAzzIQRfaN2_foJkAxyYjo=',
    # 'x-xsrftoken':'hrVqrwD1RRXZFIFSY7dpjnr31fhvwbpU',
}

response = requests.post(url="https://www.zhihu.com/api/v3/account/api/login/qrcode",headers=headers)
print(response.status_code)
print("*"*50)

for item in headers['cookie'].split(";"):
    print(item)

print(response.text)