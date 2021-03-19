+++
type = "question"
title = "Problem with smi_modules : I would like to set &quot;all&quot;"
description = '''Hi, I don&#x27;t know if it is possible, but I am working under Windows Environment with Wireshark For name resolution, I&#x27;m using smi_modules functionality, by entering the name of the MIBs I need to decode snmp logs, one by one. I would like to know if it is possible to set something like &quot;all&quot; in smi_m...'''
date = "2013-02-18T04:59:00Z"
lastmod = "2013-02-18T14:01:00Z"
weight = 18702
keywords = [ "smi" ]
aliases = [ "/questions/18702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with smi\_modules : I would like to set "all"](/questions/18702/problem-with-smi_modules-i-would-like-to-set-all)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18702-score" class="post-score" title="current number of votes">0</div><span id="post-18702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I don't know if it is possible, but I am working under Windows Environment with Wireshark For name resolution, I'm using smi_modules functionality, by entering the name of the MIBs I need to decode snmp logs, one by one. I would like to know if it is possible to set something like "all" in smi_modules file or anywhere else in order to avoid listing every MIB files I need. I would like just to specify the smi_path in which are located my mib files, and that's all. Thanks fo your reply. Regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smi" rel="tag" title="see questions tagged &#39;smi&#39;">smi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '13, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/4c75751016874aad86cd011868a0f8a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sebastien&#39;s gravatar image" /><p><span>Sebastien</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sebastien has no accepted answers">0%</span></p></div></div><div id="comments-container-18702" class="comments-container"></div><div id="comment-tools-18702" class="comment-tools"></div><div class="clear"></div><div id="comment-18702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18716"></span>

<div id="answer-container-18716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18716-score" class="post-score" title="current number of votes">1</div><span id="post-18716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Until about 5 years ago the net-SNMP library was swapped out in favor of the libsmi library. It was the net-SNMP library that could be fed with 'ALL' to make it load all MIBs. Not so for libsmi. You'll have to list all your MIBs.</p><p>But you could take a shortcut by adding them through notepad to <code>smi_modules</code> in your profile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '13, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18716" class="comments-container"></div><div id="comment-tools-18716" class="comment-tools"></div><div class="clear"></div><div id="comment-18716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

