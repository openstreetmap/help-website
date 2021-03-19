+++
type = "question"
title = "Capture Filter for DSCP 46"
description = '''How do I apply a capture filter using version 1.8.0 And what capture filter would I use to capture packets marked with DSCP 46 (EF) Thanks'''
date = "2012-08-14T10:26:00Z"
lastmod = "2012-08-14T11:34:00Z"
weight = 13619
keywords = [ "filter", "capture", "ef" ]
aliases = [ "/questions/13619" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter for DSCP 46](/questions/13619/capture-filter-for-dscp-46)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13619-score" class="post-score" title="current number of votes">0</div><span id="post-13619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I apply a capture filter using version 1.8.0 And what capture filter would I use to capture packets marked with DSCP 46 (EF)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-ef" rel="tag" title="see questions tagged &#39;ef&#39;">ef</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/c789d808f0aa0923a66fda191b0268c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VoIP%20Ready&#39;s gravatar image" /><p><span>VoIP Ready</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VoIP Ready has no accepted answers">0%</span></p></div></div><div id="comments-container-13619" class="comments-container"></div><div id="comment-tools-13619" class="comment-tools"></div><div class="clear"></div><div id="comment-13619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13621"></span>

<div id="answer-container-13621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13621-score" class="post-score" title="current number of votes">0</div><span id="post-13621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the following capture filter:</p><pre><code>(ip[1] &amp; 0xfc)&gt;&gt;2 = 46</code></pre><p>or if your traffic is vlan tagged:</p><pre><code>vlan and ((ip[1] &amp; 0xfc)&gt;&gt;2 = 46)</code></pre><p>[OK, I did not test it, but it should work theoretically :-)]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Aug '12, 10:47</strong> </span></p></div></div><div id="comments-container-13621" class="comments-container"><span id="13623"></span><div id="comment-13623" class="comment"><div id="post-13623-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks very much for the reply. It takes the filter and goes green but does not capture any packets. I am sending EF and definitley capture EF with out a filter but when I spply the above filter noting gets captured. Any further help would be greatly appreciated.</p></div><div id="comment-13623-info" class="comment-info"><span class="comment-age">(14 Aug '12, 11:08)</span> <span class="comment-user userinfo">VoIP Ready</span></div></div><span id="13624"></span><div id="comment-13624" class="comment"><div id="post-13624-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>This is what ended up working ip[1] &amp; 0xfc == 0xb8</p><p>Thanks :)</p></div><div id="comment-13624-info" class="comment-info"><span class="comment-age">(14 Aug '12, 11:25)</span> <span class="comment-user userinfo">VoIP Ready</span></div></div><span id="13625"></span><div id="comment-13625" class="comment"><div id="post-13625-score" class="comment-score"></div><div class="comment-text"><p>Weird, they should both work:</p><pre><code>$ tcpdump -d &quot;(ip[1] &amp; 0xfc)&gt;&gt;2 = 46&quot;
(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 7
(002) ldb      [15]
(003) and      #0xfc
(004) rsh      #2
(005) jeq      #0x2e            jt 6    jf 7
(006) ret      #65535
(007) ret      #0
$ tcpdump -d &quot;ip[1] &amp; 0xfc = 0xb8&quot;
(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 6
(002) ldb      [15]
(003) and      #0xfc
(004) jeq      #0xb8            jt 5    jf 6
(005) ret      #65535
(006) ret      #0
$</code></pre><p>As the value 0xb8&gt;&gt;2 = 0x2e (46)</p></div><div id="comment-13625-info" class="comment-info"><span class="comment-age">(14 Aug '12, 11:33)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="13626"></span><div id="comment-13626" class="comment"><div id="post-13626-score" class="comment-score"></div><div class="comment-text"><p>But I'm glad you got it working for you :-)</p><p>(you might want to accept my answer by clicking on the checkmark next to it, so it will not be listed on the "unanswered questions" list anymore)</p></div><div id="comment-13626-info" class="comment-info"><span class="comment-age">(14 Aug '12, 11:34)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-13621" class="comment-tools"></div><div class="clear"></div><div id="comment-13621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

