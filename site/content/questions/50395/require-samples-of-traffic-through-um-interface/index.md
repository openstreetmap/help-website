+++
type = "question"
title = "Require samples of traffic through Um interface"
description = '''Hello, My name is Radhwen, I am a software engineering student making his final year internship at the CEDRIC laboratory at CNAM, Paris. I was looking for your expertise to help me acheive a quite interesting project. I&#x27;m aiming to develop an Android application able to show the phone&#x27;s communicatio...'''
date = "2016-02-22T02:26:00Z"
lastmod = "2016-02-22T14:38:00Z"
weight = 50395
keywords = [ "sample", "um" ]
aliases = [ "/questions/50395" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Require samples of traffic through Um interface](/questions/50395/require-samples-of-traffic-through-um-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50395-score" class="post-score" title="current number of votes">0</div><span id="post-50395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, My name is Radhwen, I am a software engineering student making his final year internship at the CEDRIC laboratory at CNAM, Paris.</p><p>I was looking for your expertise to help me acheive a quite interesting project. I'm aiming to develop an Android application able to show the phone's communication's power (in dBm) during an <strong>uplink</strong> communication with the network (wether it is a 2, 3 or 4G communication) and I need to access to the data within the first <strong>physical layer</strong> in order to get the Actual MS Power level within the SACCH.</p><p>I need to get some samples of (or maybe capture by myself) the traffic that is transitting through the <strong>Um interface (the air interface between the mobile and the BTS)</strong>. It would be great to give me any hint about it's feasibility... any links/tip will be welcomed.</p><p>Thanks for reading this :) Looking to hear your response !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sample" rel="tag" title="see questions tagged &#39;sample&#39;">sample</span> <span class="post-tag tag-link-um" rel="tag" title="see questions tagged &#39;um&#39;">um</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '16, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/68c99fbbfd2d84604a14baa960e607d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Radhwen%20Khelia&#39;s gravatar image" /><p><span>Radhwen Khelia</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Radhwen Khelia has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>22 Feb '16, 02:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-50395" class="comments-container"><span id="50403"></span><div id="comment-50403" class="comment"><div id="post-50403-score" class="comment-score"></div><div class="comment-text"><p>I don't think you have access to the raw airinterfac from an Android application.</p></div><div id="comment-50403-info" class="comment-info"><span class="comment-age">(22 Feb '16, 04:48)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-50395" class="comment-tools"></div><div class="clear"></div><div id="comment-50395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50419"></span>

<div id="answer-container-50419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50419-score" class="post-score" title="current number of votes">0</div><span id="post-50419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This kind of a question is really better posted in a device developer forum such as: <a href="http://forum.xda-developers.com/">http://forum.xda-developers.com/</a></p><p>Based on the kind of information that is available via Android debug modes, it <em>might</em> be possible for an app to do this, but the question is fundamentally an Android capability question as it relates to passing/retrieving chipset information to the OS and other applications, which is kind of far away from being a Wireshark tool question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '16, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-50419" class="comments-container"></div><div id="comment-tools-50419" class="comment-tools"></div><div class="clear"></div><div id="comment-50419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

