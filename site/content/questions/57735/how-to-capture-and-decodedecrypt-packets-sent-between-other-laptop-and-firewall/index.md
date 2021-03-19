+++
type = "question"
title = "How to capture and decode/decrypt packets sent between other laptop and firewall ?"
description = '''Hello,  I&#x27;m totaly new here and also new to Wireshark. I don&#x27;t speak English natively, so my apologies for my bad English.  As ICT employee at an elementary school I recently discovered unauthorized access (unknown MAC - not from a school pc) to our firewall through one of the admin accounts. Using ...'''
date = "2016-11-30T11:58:00Z"
lastmod = "2016-12-02T02:44:00Z"
weight = 57735
keywords = [ "firewall", "pc", "other", "urlencoded" ]
aliases = [ "/questions/57735" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture and decode/decrypt packets sent between other laptop and firewall ?](/questions/57735/how-to-capture-and-decodedecrypt-packets-sent-between-other-laptop-and-firewall)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57735-score" class="post-score" title="current number of votes">0</div><span id="post-57735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm totaly new here and also new to Wireshark. I don't speak English natively, so my apologies for my bad English.</p><p>As ICT employee at an elementary school I recently discovered unauthorized access (unknown MAC - not from a school pc) to our firewall through one of the admin accounts. Using Wireshark I have been able to track down the packets sent during this unauthorized access, but unfortunately Wireshark couldn't retrieve the credentials so I don't know which admin account is compromised. I encountered the output "application/x-www-form-urlencoded". Regrettably I haven't been able yet to find out how to unveil the used login and password.</p><p>Can somebody please tell me how to decode or decrypt the "application/x-www-form-urlencoded" output in Wireshark ?</p><p>edit: cropped screenshot removed due to security reasons.</p><p>Thanks a lot in advance.</p><p>Kind regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-pc" rel="tag" title="see questions tagged &#39;pc&#39;">pc</span> <span class="post-tag tag-link-other" rel="tag" title="see questions tagged &#39;other&#39;">other</span> <span class="post-tag tag-link-urlencoded" rel="tag" title="see questions tagged &#39;urlencoded&#39;">urlencoded</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '16, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/139a11975d294900dc2e5212a3c03891?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ikke&#39;s gravatar image" /><p><span>Ikke</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ikke has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Dec '16, 09:03</strong> </span></p></div></div><div id="comments-container-57735" class="comments-container"></div><div id="comment-tools-57735" class="comment-tools"></div><div class="clear"></div><div id="comment-57735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57739"></span>

<div id="answer-container-57739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57739-score" class="post-score" title="current number of votes">0</div><span id="post-57739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that the username and password entered are in the form items "un" and "pw" respectively, they look like <a href="https://en.wikipedia.org/wiki/Base64">Base64</a> encoded values to me.</p><p>Decoding them is trivial, e.g. using this <a href="https://www.base64decode.org/">Base 64 decoder</a>. I won't post the actual values here in case you still need to secure the account, but anyone else looking at your image could easily do so, so best to secure that account ASAP.</p><p>Whatever system is producing these login pages seems very insecure to me (hopefully it's protected by a TLS tunnel) as Base64 encoding is NOT encrypting the credentials.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '16, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57739" class="comments-container"><span id="57743"></span><div id="comment-57743" class="comment"><div id="post-57743-score" class="comment-score"></div><div class="comment-text"><p>Insecure indeed. Anyone with a Dutch (Flemisch) dictionary attack would get in.</p></div><div id="comment-57743-info" class="comment-info"><span class="comment-age">(30 Nov '16, 22:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57768"></span><div id="comment-57768" class="comment"><div id="post-57768-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p><span></span><span>@grahamb</span> Thanks for the quick reply. After reading the links in your answer, I can confirm that the username and password are indeed Base64 encoded. Since the used credentials are different from my login credentials I'm sure mine are not compromised. The login page belongs to a juniper ssg5 firewall (indeed protected by a TLS tunnel).<br />
</p><p><span></span><span>@grahamb</span> and <span>@Jaap</span> I know this is very insecure. I have already reported this to the ICT administrator. He promised me to take care of it. Since nor our wan ip nor our mac address are posted here, should I remove the cropped screenshot in my initial post ? My biggest question is now: How has the unauthorized "visitor" managed to give himself a admin login ?</p><p>Thanks in advance.</p><p>Kind regards.</p></div><div id="comment-57768-info" class="comment-info"><span class="comment-age">(01 Dec '16, 11:41)</span> <span class="comment-user userinfo">Ikke</span></div></div><span id="57782"></span><div id="comment-57782" class="comment"><div id="post-57782-score" class="comment-score"></div><div class="comment-text"><p><span>@Ikke</span>, it's a judgement call for you whether you leave the image up, personally I wouldn't as it does leak sensitive info about your site. If you do remove it, please edit your question to indicate what has happened for others.</p></div><div id="comment-57782-info" class="comment-info"><span class="comment-age">(02 Dec '16, 02:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-57739" class="comment-tools"></div><div class="clear"></div><div id="comment-57739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

