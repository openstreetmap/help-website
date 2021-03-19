+++
type = "question"
title = "Trouble with 802.11 decryption key formats"
description = '''Hi! I will try to make this simple, but recently I have been playing around with decrypting 802.11 packets on Wireshark for Mac OS. I had successfully done it many times on my other network, however when I tried it on my main network I noticed that the decryption process failed. If I am correct it i...'''
date = "2016-12-15T15:25:00Z"
lastmod = "2016-12-16T13:43:00Z"
weight = 58151
keywords = [ "decryption", "802.11", "key", "format" ]
aliases = [ "/questions/58151" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Trouble with 802.11 decryption key formats](/questions/58151/trouble-with-80211-decryption-key-formats)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58151-score" class="post-score" title="current number of votes">0</div><span id="post-58151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I will try to make this simple, but recently I have been playing around with decrypting 802.11 packets on Wireshark for Mac OS. I had successfully done it many times on my other network, however when I tried it on my main network I noticed that the decryption process failed. If I am correct it is because my SSID on my main network uses spaces and a minus symbol "-". How would I format the key to work even with the spaces and "-" symbol?</p><p>This is a similar make of my key that I am attempting to use</p><p>wpa-pwd: coolpasswordhere:cool bssid-here</p><p>This is a similar make of my previous key I used with my other network</p><p>wpa-pwd: coolpasswordhere:bssidhere</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '16, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/704bcf7719ffb8ba992f9a8da20c0155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milorules1012&#39;s gravatar image" /><p><span>milorules1012</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milorules1012 has no accepted answers">0%</span></p></div></div><div id="comments-container-58151" class="comments-container"></div><div id="comment-tools-58151" class="comment-tools"></div><div class="clear"></div><div id="comment-58151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58161"></span>

<div id="answer-container-58161" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58161-score" class="post-score" title="current number of votes">1</div><span id="post-58161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="milorules1012 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't use special characters in my SSID names so do not run into this particular problem. However, a workaround might be to use an offline PMK generator such as</p><p><a href="https://www.wireshark.org/tools/wpa-psk.html">https://www.wireshark.org/tools/wpa-psk.html</a></p><p>and then use these results in Wireshark as WPA-PSK entry instead of WPA-PWD:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/WPA_PSK_Generator.png" alt="alt text" /></p><p>Copy the generated PSK into Wireshark:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Decryption_Key_Management.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '16, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></img></div></div><div id="comments-container-58161" class="comments-container"><span id="58175"></span><div id="comment-58175" class="comment"><div id="post-58175-score" class="comment-score"></div><div class="comment-text"><p>This works and now I know what that option does too! Thanks for the help!</p></div><div id="comment-58175-info" class="comment-info"><span class="comment-age">(16 Dec '16, 13:43)</span> <span class="comment-user userinfo">milorules1012</span></div></div></div><div id="comment-tools-58161" class="comment-tools"></div><div class="clear"></div><div id="comment-58161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

