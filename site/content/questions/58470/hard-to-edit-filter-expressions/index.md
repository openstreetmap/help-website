+++
type = "question"
title = "Hard to edit filter expressions"
description = '''Hello, I tried to use Wireshark to capture traffic to a certain website (on Windows). It is very hard to edit filter expression in the top bar after you enter it. For example, arrows key don&#x27;t work at all, same with Home and End keys. Using any of those results in losing input focus. Basically, if I...'''
date = "2017-01-02T23:49:00Z"
lastmod = "2017-01-03T10:33:00Z"
weight = 58470
keywords = [ "filter" ]
aliases = [ "/questions/58470" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Hard to edit filter expressions](/questions/58470/hard-to-edit-filter-expressions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58470-score" class="post-score" title="current number of votes">0</div><span id="post-58470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I tried to use Wireshark to capture traffic to a certain website (on Windows). It is very hard to edit filter expression in the top bar after you enter it. For example, arrows key don't work at all, same with Home and End keys. Using any of those results in losing input focus. Basically, if I want to change a typo I have to delete the whole thing and type everything again (or copy &amp; paste).</p><p>Am I doing something wrong or it's a bug?</p><p>I'm new to Wireshark, I used an HTTP proxy before all this (Fiddler) but I needed to inspect traffic for an app that doesn't honor system proxy settings :/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '17, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/5856bdbda75b8bec4fb405280390b83d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiredude&#39;s gravatar image" /><p><span>wiredude</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiredude has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '17, 23:52</strong> </span></p></div></div><div id="comments-container-58470" class="comments-container"><span id="58471"></span><div id="comment-58471" class="comment"><div id="post-58471-score" class="comment-score"></div><div class="comment-text"><p>Are you editing the filter after capture is stopped, or is it still running?</p></div><div id="comment-58471-info" class="comment-info"><span class="comment-age">(03 Jan '17, 03:05)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="58472"></span><div id="comment-58472" class="comment"><div id="post-58472-score" class="comment-score"></div><div class="comment-text"><p>I can reproduce this too on the Qt version, but not on legacy GTK. I'm relatively current with version 2.2.3 but have seen this for quite a while. It happens often, but I do not know the exact sequence to get in this state. Recovery is usually to delete the entry and start over.</p></div><div id="comment-58472-info" class="comment-info"><span class="comment-age">(03 Jan '17, 03:21)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="58473"></span><div id="comment-58473" class="comment"><div id="post-58473-score" class="comment-score"></div><div class="comment-text"><p>I'm editing while capture is running. I'm using the latest version of Wireshark on Windows 10. I've also just checked on Ubuntu and it's happening there too, with Wireshark 2.2.0.</p></div><div id="comment-58473-info" class="comment-info"><span class="comment-age">(03 Jan '17, 03:29)</span> <span class="comment-user userinfo">wiredude</span></div></div><span id="58474"></span><div id="comment-58474" class="comment"><div id="post-58474-score" class="comment-score"></div><div class="comment-text"><p>When capture is stopped I can edit filter text without problems. I guess it's a bug then.</p></div><div id="comment-58474-info" class="comment-info"><span class="comment-age">(03 Jan '17, 03:31)</span> <span class="comment-user userinfo">wiredude</span></div></div></div><div id="comment-tools-58470" class="comment-tools"></div><div class="clear"></div><div id="comment-58470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58480"></span>

<div id="answer-container-58480" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58480-score" class="post-score" title="current number of votes">2</div><span id="post-58480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiredude has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(Just to provide an answer.)</p><p>This sounds like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11890">bug 11890</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '17, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58480" class="comments-container"><span id="58481"></span><div id="comment-58481" class="comment"><div id="post-58481-score" class="comment-score"></div><div class="comment-text"><p>That smells like it. Thanks for looking it up - it was not annoying enough to chase it down.</p></div><div id="comment-58481-info" class="comment-info"><span class="comment-age">(03 Jan '17, 07:53)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="58485"></span><div id="comment-58485" class="comment"><div id="post-58485-score" class="comment-score"></div><div class="comment-text"><p>No problem - I like helping to avoid duplicate bug reports when I can (not that I've had time to look at the bugs database in a while...). And I like questions with answers. :-)</p></div><div id="comment-58485-info" class="comment-info"><span class="comment-age">(03 Jan '17, 10:33)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-58480" class="comment-tools"></div><div class="clear"></div><div id="comment-58480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

