+++
type = "question"
title = "What is &quot;Type 21 error&quot; in SSL Encryption Alerts ?"
description = '''Can anybody explain what &quot;Type 21 error&quot; means in Encryption Alert packages? Any reference to the protocol specs concerning these Alerts would be appreciated. Example here: https://www.cloudshark.org/captures/efebf7bba359'''
date = "2016-02-13T03:39:00Z"
lastmod = "2016-02-15T06:17:00Z"
weight = 50168
keywords = [ "ssl", "tlsv1.2", "error" ]
aliases = [ "/questions/50168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is "Type 21 error" in SSL Encryption Alerts ?](/questions/50168/what-is-type-21-error-in-ssl-encryption-alerts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50168-score" class="post-score" title="current number of votes">0</div><span id="post-50168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anybody explain what "Type 21 error" means in Encryption Alert packages? Any reference to the protocol specs concerning these Alerts would be appreciated.</p><p>Example here: <a href="https://www.cloudshark.org/captures/efebf7bba359">https://www.cloudshark.org/captures/efebf7bba359</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tlsv1.2" rel="tag" title="see questions tagged &#39;tlsv1.2&#39;">tlsv1.2</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '16, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/653d979a2dc2892e289024f6a619921e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boiiingg&#39;s gravatar image" /><p><span>boiiingg</span><br />
<span class="score" title="2 reputation points">2</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boiiingg has no accepted answers">0%</span></p></div></div><div id="comments-container-50168" class="comments-container"><span id="50171"></span><div id="comment-50171" class="comment"><div id="post-50171-score" class="comment-score"></div><div class="comment-text"><p>BTW. If this "type 21" behaviour is according to specs, then different semantics in Wireshark would be an idea?</p></div><div id="comment-50171-info" class="comment-info"><span class="comment-age">(13 Feb '16, 04:04)</span> <span class="comment-user userinfo">boiiingg</span></div></div></div><div id="comment-tools-50168" class="comment-tools"></div><div class="clear"></div><div id="comment-50168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50185"></span>

<div id="answer-container-50185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50185-score" class="post-score" title="current number of votes">1</div><span id="post-50185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What are you expecting to see? Type 21 is the TLS record type for an Alert Message which is always encrypted.<br />
</p><p>Unless you have supplied sufficient keying material to allow Wireshark to decrypt the alert, that's all Wireshark can report.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '16, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-50185" class="comments-container"><span id="50200"></span><div id="comment-50200" class="comment"><div id="post-50200-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. I was looking for that actually. But where do I extract the keying info? I've got some experience with decrypting SSL streams having webserver keypairs, importing them in Wireshark. But I don't know if there is a way to obtain keying data from the clientside (for i.e. is there a browser-plugin that can export session keys for analysis?)</p></div><div id="comment-50200-info" class="comment-info"><span class="comment-age">(15 Feb '16, 00:46)</span> <span class="comment-user userinfo">boiiingg</span></div></div><span id="50203"></span><div id="comment-50203" class="comment"><div id="post-50203-score" class="comment-score"></div><div class="comment-text"><p>That's a separate Question, but as it has already been asked several times, please don't ask it once more and look through this site for "pre-master key log file export".</p></div><div id="comment-50203-info" class="comment-info"><span class="comment-age">(15 Feb '16, 01:15)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50209"></span><div id="comment-50209" class="comment"><div id="post-50209-score" class="comment-score">1</div><div class="comment-text"><p>Also see the Wiki page on SSL, especially the section on decrypting with a <a href="https://wiki.wireshark.org/SSL#Using_the_.28Pre.29-Master-Secret">pre-master secret</a>.</p></div><div id="comment-50209-info" class="comment-info"><span class="comment-age">(15 Feb '16, 06:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-50185" class="comment-tools"></div><div class="clear"></div><div id="comment-50185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

