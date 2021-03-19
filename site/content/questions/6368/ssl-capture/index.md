+++
type = "question"
title = "SSL capture"
description = '''I have my SSL client&#x27;s encrypted RSA key. I&#x27;m trying to capture the SSL traffic on a PC in the network. I understand that there are some settings I need to do on the wireshark or decrypt key. Please help me on how to do this. Thanks a lot '''
date = "2011-09-14T13:11:00Z"
lastmod = "2011-09-15T08:52:00Z"
weight = 6368
keywords = [ "ssl" ]
aliases = [ "/questions/6368" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL capture](/questions/6368/ssl-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6368-score" class="post-score" title="current number of votes">0</div><span id="post-6368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have my SSL client's encrypted RSA key. I'm trying to capture the SSL traffic on a PC in the network. I understand that there are some settings I need to do on the wireshark or decrypt key. Please help me on how to do this.</p><p>Thanks a lot</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '11, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/9839d93b39ae5543f612103c8e2d9b31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jennyliusd&#39;s gravatar image" /><p><span>jennyliusd</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jennyliusd has no accepted answers">0%</span></p></div></div><div id="comments-container-6368" class="comments-container"></div><div id="comment-tools-6368" class="comment-tools"></div><div class="clear"></div><div id="comment-6368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6369"></span>

<div id="answer-container-6369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6369-score" class="post-score" title="current number of votes">1</div><span id="post-6369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sake did an much referenced presentation at Sharkfest'09 on the subject. <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">Check it out</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6369" class="comments-container"><span id="6373"></span><div id="comment-6373" class="comment"><div id="post-6373-score" class="comment-score"></div><div class="comment-text"><p>:-) Thx for the reference Jaap!</p></div><div id="comment-6373-info" class="comment-info"><span class="comment-age">(14 Sep '11, 15:11)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="6375"></span><div id="comment-6375" class="comment"><div id="post-6375-score" class="comment-score"></div><div class="comment-text"><p>Thx for the doc. It is very helpful. But I'm confused on removing the passphrase. Where do I type the command? On page 56: <span class="__cf_email__" data-cfemail="b9cbd6d6cdf9d4ded4cd">[email protected]</span># openssl rsa -in encrypted.key -out cleartext.key</p><p>Enter pass phrase for encrypted.key: &lt;passphrase&gt;</p><p>writing RSA key</p><p><span class="__cf_email__" data-cfemail="b9cbd6d6cdf9d4ded4cd">[email protected]</span>#</p><p>Where do I find the &lt;passphrase&gt;?</p><p>Thank you.</p></div><div id="comment-6375-info" class="comment-info"><span class="comment-age">(14 Sep '11, 17:00)</span> <span class="comment-user userinfo">jennyliusd</span></div></div><span id="6376"></span><div id="comment-6376" class="comment"><div id="post-6376-score" class="comment-score"></div><div class="comment-text"><p>If the key is encrypted with a passphrase, then the administrator that provided the key to you will have the passphrase.</p></div><div id="comment-6376-info" class="comment-info"><span class="comment-age">(14 Sep '11, 17:11)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="6393"></span><div id="comment-6393" class="comment"><div id="post-6393-score" class="comment-score"></div><div class="comment-text"><p>Do I need this for Server's key or Client's key? Sounds like I need the decrypted Server's RSA key on Wireshark, right?</p></div><div id="comment-6393-info" class="comment-info"><span class="comment-age">(15 Sep '11, 08:25)</span> <span class="comment-user userinfo">jennyliusd</span></div></div><span id="6395"></span><div id="comment-6395" class="comment"><div id="post-6395-score" class="comment-score"></div><div class="comment-text"><p>On wireshark preference settings: ssl.keys_list: 192.168.3.3,443,http,c:key.pem</p><p>Is the IP address for my PC or the server?</p><p>Thank you.</p></div><div id="comment-6395-info" class="comment-info"><span class="comment-age">(15 Sep '11, 08:35)</span> <span class="comment-user userinfo">jennyliusd</span></div></div><span id="6397"></span><div id="comment-6397" class="comment not_top_scorer"><div id="post-6397-score" class="comment-score"></div><div class="comment-text"><p>You will need the (decrypted) private key of the server. And in the preferences you will use the server IP address, not the client IP address.</p></div><div id="comment-6397-info" class="comment-info"><span class="comment-age">(15 Sep '11, 08:52)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-6369" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-6369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

