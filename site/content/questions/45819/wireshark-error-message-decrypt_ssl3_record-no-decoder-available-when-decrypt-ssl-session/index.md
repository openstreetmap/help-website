+++
type = "question"
title = "Wireshark error message &quot;decrypt_ssl3_record: no decoder available&quot; when decrypt SSL session"
description = '''I have a pcap of a HTTPS session. When trying to decrypt it, it complained about &quot;decrypt_ssl3_record: no decoder available&quot;.  I have made sure I am not using DHE based cipher, but still getting the above message. Wonder what cipher is supported by Wireshark (ver 1.8.2). Here is the debug file.'''
date = "2015-09-12T22:08:00Z"
lastmod = "2015-09-15T14:50:00Z"
weight = 45819
keywords = [ "wireshark" ]
aliases = [ "/questions/45819" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark error message "decrypt\_ssl3\_record: no decoder available" when decrypt SSL session](/questions/45819/wireshark-error-message-decrypt_ssl3_record-no-decoder-available-when-decrypt-ssl-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45819-score" class="post-score" title="current number of votes">0</div><span id="post-45819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a <a href="https://www.cloudshark.org/captures/efbcd03eab1a">pcap</a> of a HTTPS session. When trying to decrypt it, it complained about "decrypt_ssl3_record: no decoder available". I have made sure I am not using DHE based cipher, but still getting the above message.<br />
Wonder what cipher is supported by Wireshark (ver 1.8.2). Here is the <a href="http://pastebin.com/h0785i8R">debug file</a>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '15, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></p></div></div><div id="comments-container-45819" class="comments-container"><span id="45861"></span><div id="comment-45861" class="comment"><div id="post-45861-score" class="comment-score"></div><div class="comment-text"><p>Can you try the latest development version of Wireshark? Either your private key is wrong or you are affected by a very specific bug which is fixed in the development version (<a href="https://code.wireshark.org/review/9573).">https://code.wireshark.org/review/9573).</a></p></div><div id="comment-45861-info" class="comment-info"><span class="comment-age">(15 Sep '15, 14:02)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="45865"></span><div id="comment-45865" class="comment"><div id="post-45865-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@lekensteyn</span> for the suggestion, I just downloaded the source and built it, still has the error "decrypt_ssl3_record: no decoder available". The pcap file URL is in the question, the cert and priviate key is here: <a href="http://pastebin.com/2ZX9b1Pj">http://pastebin.com/2ZX9b1Pj</a> Thanks!</p></div><div id="comment-45865-info" class="comment-info"><span class="comment-age">(15 Sep '15, 14:50)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-45819" class="comment-tools"></div><div class="clear"></div><div id="comment-45819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

