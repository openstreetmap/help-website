+++
type = "question"
title = "Debugging the web slowness ."
description = '''I was investigating a very intermittent slowness issue of a web application where I see one of my static file (this is not fixed file like for example some time x.js and some time y.css) gets hung up for 8 minute around. I see this (8 minute )time in fiddler request statistics where serverconnected ...'''
date = "2014-10-11T14:46:00Z"
lastmod = "2014-10-21T07:06:00Z"
weight = 36977
keywords = [ "network", "slowness", "wireshark" ]
aliases = [ "/questions/36977" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Debugging the web slowness .](/questions/36977/debugging-the-web-slowness)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36977-score" class="post-score" title="current number of votes">0</div><span id="post-36977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was investigating a very intermittent slowness issue of a web application where I see one of my static file (this is not fixed file like for example some time x.js and some time y.css) gets hung up for 8 minute around. I see this (8 minute )time in fiddler request statistics where serverconnected time is displayed almost after 8 minute of client done request. Although looking On server I find sever serves the file in milliseconds after receiving request( 8 minute later from client request).</p><p>On further looking at fiddler I found that slow request try to reuse the existing connection and it fails after 8 minute around and make new connection. I am not sure if 8.2 minute is some time out value of anything.</p><p>I took the tcpdump of that scenario and looking at expert info where I found this request in chat tab and It is showing two frames.On "Follow TCP stream" for First frame I see request is listed but no response below that.</p><p>Can some one get some idea about probable reason (or debugging info ) of where the request was hung. is it Tcp connection time out ? or something else . Any help will be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-slowness" rel="tag" title="see questions tagged &#39;slowness&#39;">slowness</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '14, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/4470766dea58f3c8e4726011ad32ad77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mann2409&#39;s gravatar image" /><p><span>mann2409</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mann2409 has no accepted answers">0%</span></p></div></div><div id="comments-container-36977" class="comments-container"><span id="37237"></span><div id="comment-37237" class="comment"><div id="post-37237-score" class="comment-score"></div><div class="comment-text"><blockquote><p><strong>Can some one get some idea about probable reason</strong> (or debugging info ) of where the request was hung.</p></blockquote><p>without looking at the capture file? Well .... if I was able to do that, I could probably earn a lot of money through, let's call it "remote viewing" ;-)</p><p>Seriously: The (most plausible) reason why nobody answered your question yet is this: You are not providing enough information to give any meaningful answer. So, if you want anybody to dive further into this, please upload the capture file somewhere and post the link here. Then add some details about the TCP stream (in the capture file) that could be "problematic" based on your analysis (IP/ports/stream number), etc.</p><p>After all: I'm sure you'll find somebody here who is able to help you with that :-)</p><p>Regards<br />
Kurt</p></div><div id="comment-37237-info" class="comment-info"><span class="comment-age">(21 Oct '14, 07:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-36977" class="comment-tools"></div><div class="clear"></div><div id="comment-36977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

