+++
type = "question"
title = "How to define and use alias for custom display filter?"
description = '''Hi I&#x27;m using Wireshark with long display filers e.g (wlan_mgt.fixed.status_code == 0x0000) &amp;amp;&amp;amp; (wlan.fc.type_subtype == 0x0b) and switch between them many times. Can I define alias for these filters, i.e I enter myfilter1 instead of (wlan_mgt.fixed.status_code == 0x0000) &amp;amp;&amp;amp; (wlan.fc.t...'''
date = "2017-04-10T00:01:00Z"
lastmod = "2017-04-10T08:12:00Z"
weight = 60694
keywords = [ "wireshark", "display-filter" ]
aliases = [ "/questions/60694" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to define and use alias for custom display filter?](/questions/60694/how-to-define-and-use-alias-for-custom-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60694-score" class="post-score" title="current number of votes">0</div><span id="post-60694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm using Wireshark with long display filers e.g <code>(wlan_mgt.fixed.status_code == 0x0000) &amp;&amp; (wlan.fc.type_subtype == 0x0b)</code> and switch between them many times. Can I define alias for these filters, i.e I enter <code>myfilter1</code> instead of <code>(wlan_mgt.fixed.status_code == 0x0000) &amp;&amp; (wlan.fc.type_subtype == 0x0b)</code>?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '17, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/71d18146e011b67e81934ee506cf6b08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SuBCo&#39;s gravatar image" /><p><span>SuBCo</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SuBCo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '17, 00:02</strong> </span></p></div></div><div id="comments-container-60694" class="comments-container"></div><div id="comment-tools-60694" class="comment-tools"></div><div class="clear"></div><div id="comment-60694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60700"></span>

<div id="answer-container-60700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60700-score" class="post-score" title="current number of votes">0</div><span id="post-60700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, go to Analyze -&gt; Display Filters to get a dialog that allow you to enter filters and give them a meaningful name. Unfortunately, it seems that in the Qt version you can't then apply those filters :-(</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '17, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60700" class="comments-container"><span id="60704"></span><div id="comment-60704" class="comment"><div id="post-60704-score" class="comment-score"></div><div class="comment-text"><p>How should i use them? Can I do logical operation with them like: and, or, not</p></div><div id="comment-60704-info" class="comment-info"><span class="comment-age">(10 Apr '17, 07:33)</span> <span class="comment-user userinfo">SuBCo</span></div></div><span id="60705"></span><div id="comment-60705" class="comment"><div id="post-60705-score" class="comment-score"></div><div class="comment-text"><p>I think there's a bug in the GUI, in the old GTK version any selected filter would be used on clicking "OK" on the dialog. You could also click "Apply" to apply the filter and keep the dialog open.</p></div><div id="comment-60705-info" class="comment-info"><span class="comment-age">(10 Apr '17, 08:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60700" class="comment-tools"></div><div class="clear"></div><div id="comment-60700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

