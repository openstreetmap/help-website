+++
type = "question"
title = "Tshark column fields"
description = '''I using Wireshark on Ubuntu 12.04 and whenever i type in the field such as -e col.Protocol , col.Info etc.. i could not get any result display on text editor or csv file. Anyone know what is the problem?'''
date = "2014-05-06T19:54:00Z"
lastmod = "2014-06-19T16:50:00Z"
weight = 32574
keywords = [ "column" ]
aliases = [ "/questions/32574" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark column fields](/questions/32574/tshark-column-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32574-score" class="post-score" title="current number of votes">0</div><span id="post-32574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I using Wireshark on Ubuntu 12.04 and whenever i type in the field such as -e col.Protocol , col.Info etc.. i could not get any result display on text editor or csv file. Anyone know what is the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 19:54</strong></p><img src="https://secure.gravatar.com/avatar/beec851e7379ace745a11fbb7d48e4d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tch&#39;s gravatar image" /><p><span>tch</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tch has no accepted answers">0%</span></p></div></div><div id="comments-container-32574" class="comments-container"><span id="32599"></span><div id="comment-32599" class="comment"><div id="post-32599-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark are you using?</p></div><div id="comment-32599-info" class="comment-info"><span class="comment-age">(07 May '14, 07:19)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="32627"></span><div id="comment-32627" class="comment"><div id="post-32627-score" class="comment-score"></div><div class="comment-text"><p>wireshark 1.6.7 is it the latest? Sorry for asking so much as i am new to it</p></div><div id="comment-32627-info" class="comment-info"><span class="comment-age">(07 May '14, 17:51)</span> <span class="comment-user userinfo">tch</span></div></div><span id="32643"></span><div id="comment-32643" class="comment"><div id="post-32643-score" class="comment-score"></div><div class="comment-text"><p>No, Wireshark 1.6.7 is most definitely not the latest available version. The latest releases as of this writing are:</p><ul><li>Stable: 1.10.7</li><li>Old Stable: 1.8.14</li><li>Development: 1.11.3</li></ul><p>You can download them from <a href="http://www.wireshark.org/download.html">http://www.wireshark.org/download.html</a>.</p><p>The 1.6 branch went End-Of-Life on June 7, 2013. Refer to the <a href="http://wiki.wireshark.org/Development/LifeCycle">LifeCycle</a> page for more information about End-Of-Life planning.</p></div><div id="comment-32643-info" class="comment-info"><span class="comment-age">(08 May '14, 07:20)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-32574" class="comment-tools"></div><div class="clear"></div><div id="comment-32574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32698"></span>

<div id="answer-container-32698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32698-score" class="post-score" title="current number of votes">3</div><span id="post-32698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So the answer to your question is simple. Version 1.6.7 doesn't support <code>-e col.*</code>. You need to upgrade to a version of Wireshark that does support it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-32698" class="comments-container"></div><div id="comment-tools-32698" class="comment-tools"></div><div class="clear"></div><div id="comment-32698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33969"></span>

<div id="answer-container-33969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33969-score" class="post-score" title="current number of votes">2</div><span id="post-33969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As of the 1.11.x and 1.12 versions of tshark, the field names are "_ws.col.Protocol" and "_ws.col.Info", instead of "col.Protocol" and "col.Info".</p><p>Example:</p><p><code>tshark -T fields -e _ws.col.Protocol -e _ws.col.Info</code></p><p>Source: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/028a4be69999143f43a3ed2e97f42159?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CraigGarrett&#39;s gravatar image" /><p><span>CraigGarrett</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CraigGarrett has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '14, 10:21</strong> </span></p></div></div><div id="comments-container-33969" class="comments-container"></div><div id="comment-tools-33969" class="comment-tools"></div><div class="clear"></div><div id="comment-33969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

