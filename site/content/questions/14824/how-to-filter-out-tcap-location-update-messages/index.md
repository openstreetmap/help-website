+++
type = "question"
title = "how to filter out tcap location update messages"
description = '''Hi All, I want to filter out these wireshark messages. They are always coming, does anyone know how to filter below messages out? *GSM MAP invoke subscriberLocationReport  GSM MAP returnResultLast subscriberLocationReport  GSM MAP invoke provideSubscriberLocation*  '''
date = "2012-10-09T10:35:00Z"
lastmod = "2012-10-10T13:47:00Z"
weight = 14824
keywords = [ "tcap", "map", "gsm", "filter", "out" ]
aliases = [ "/questions/14824" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to filter out tcap location update messages](/questions/14824/how-to-filter-out-tcap-location-update-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14824-score" class="post-score" title="current number of votes">0</div><span id="post-14824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I want to filter out these wireshark messages. They are always coming, does anyone know how to filter below messages out?</p><p><strong><em>*</em></strong>GSM MAP invoke subscriberLocationReport<br />
</p><p>GSM MAP returnResultLast subscriberLocationReport</p><p>GSM MAP invoke provideSubscriberLocation<strong><em>*</em></strong><br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcap" rel="tag" title="see questions tagged &#39;tcap&#39;">tcap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/06a06257813cd3d00ec97ce152311a5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="omer&#39;s gravatar image" /><p><span>omer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="omer has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Oct '12, 10:35</strong> </span></p></div></div><div id="comments-container-14824" class="comments-container"></div><div id="comment-tools-14824" class="comment-tools"></div><div class="clear"></div><div id="comment-14824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14905"></span>

<div id="answer-container-14905" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14905-score" class="post-score" title="current number of votes">1</div><span id="post-14905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="omer has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In general if you want to filter out something, find the thing you're interested in (e.g., subscriberLocationReport) in the decode tree, right-click on it, and select "Apply (or "Prepare") as filter" and then select "Not selected."</p><p>For an updateLocation (sorry, I couldn't easily find any examples of the messages you mentioned), the resulting filter is:</p><p>!(gsm_old.localValue == 2)</p><p>Of course you can build up more complicated filters like this (which filters out updateLocation and updateGprsLocation):</p><p>!(gsm_old.localValue == 2) &amp;&amp; !(gsm_old.localValue == 23)</p><p>To find these values in a GSM message, look here:</p><pre><code>GSM Mobile Application
    Component: invoke (1)
        invoke
            invokeID: 15
            opCode: localValue (0)
                localValue: updateLocation (2) &lt;&lt;&lt; right-click on this field to filter out updateLocations</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-14905" class="comments-container"></div><div id="comment-tools-14905" class="comment-tools"></div><div class="clear"></div><div id="comment-14905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

