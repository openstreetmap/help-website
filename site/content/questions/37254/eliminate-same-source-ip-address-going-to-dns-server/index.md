+++
type = "question"
title = "Eliminate same source ip address going to dns server"
description = '''I&#x27;m trying to isolate who is still hitting our old dns server and a bunch of packets left over after running editcap -p, clearing bad requests, and broadcast traffic. I see the same IP hitting the dns server but with different requests and/or packets. How do I keep the first time the source was capt...'''
date = "2014-10-21T12:58:00Z"
lastmod = "2014-11-21T07:36:00Z"
weight = 37254
keywords = [ "duplicatedsource" ]
aliases = [ "/questions/37254" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Eliminate same source ip address going to dns server](/questions/37254/eliminate-same-source-ip-address-going-to-dns-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37254-score" class="post-score" title="current number of votes">0</div><span id="post-37254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to isolate who is still hitting our old dns server and a bunch of packets left over after running editcap -p, clearing bad requests, and broadcast traffic. I see the same IP hitting the dns server but with different requests and/or packets. How do I keep the first time the source was captured and deleted the duplicated source ip addresses? Is there a way to clear duplicated source ip addresses instead of packets?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicatedsource" rel="tag" title="see questions tagged &#39;duplicatedsource&#39;">duplicatedsource</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/da0b4deeddffb3d44d92d058bd852fd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xxlunarxx&#39;s gravatar image" /><p><span>xxlunarxx</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xxlunarxx has no accepted answers">0%</span></p></div></div><div id="comments-container-37254" class="comments-container"></div><div id="comment-tools-37254" class="comment-tools"></div><div class="clear"></div><div id="comment-37254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37255"></span>

<div id="answer-container-37255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37255-score" class="post-score" title="current number of votes">1</div><span id="post-37255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want a list of unique IP addresses you might want to use tshark with the "-T fields" parameter instead, and using the "ip.src" field, like</p><pre><code>tshark -r &quot;yourtrace.pcapng&quot; -T fields -e ip.src | sort | uniq</code></pre><p>You need the unix style command line tools "sort" and "uniq" of course, or in your case at least "uniq".</p><p>Or, you could just use Wireshark, filter on DNS and use the endpoint statistics to list all IP addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '14, 13:09</strong> </span></p></div></div><div id="comments-container-37255" class="comments-container"><span id="37257"></span><div id="comment-37257" class="comment"><div id="post-37257-score" class="comment-score"></div><div class="comment-text"><p>what kind of filter can i use in wireshark that would be the same as the 'uniq' option. I'm running wireshark on our old dns server which is windows.</p></div><div id="comment-37257-info" class="comment-info"><span class="comment-age">(21 Oct '14, 14:24)</span> <span class="comment-user userinfo">xxlunarxx</span></div></div><span id="38046"></span><div id="comment-38046" class="comment"><div id="post-38046-score" class="comment-score"></div><div class="comment-text"><p>This line worked. Thanks mate.</p></div><div id="comment-38046-info" class="comment-info"><span class="comment-age">(21 Nov '14, 07:36)</span> <span class="comment-user userinfo">xxlunarxx</span></div></div></div><div id="comment-tools-37255" class="comment-tools"></div><div class="clear"></div><div id="comment-37255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

