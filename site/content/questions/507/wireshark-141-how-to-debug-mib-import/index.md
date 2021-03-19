+++
type = "question"
title = "Wireshark 1.4.1 - how to debug MIB import?"
description = '''Using Wireshark 1.4.1 on Windows XP Pro SP3; trying to import a vendor MIB in order to decode content of some SNMP traps etc. After importing the MIB and restarting Wireshark the following error box pops up: &quot;Stopped processing module ARTEVEA-MIB due to error(s) to prevent potential crash in libsmi....'''
date = "2010-10-14T03:38:00Z"
lastmod = "2010-10-15T03:04:00Z"
weight = 507
keywords = [ "mib", "snmp" ]
aliases = [ "/questions/507" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.4.1 - how to debug MIB import?](/questions/507/wireshark-141-how-to-debug-mib-import)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-507-score" class="post-score" title="current number of votes">0</div><span id="post-507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark 1.4.1 on Windows XP Pro SP3; trying to import a vendor MIB in order to decode content of some SNMP traps etc.</p><p>After importing the MIB and restarting Wireshark the following error box pops up:</p><p>"Stopped processing module ARTEVEA-MIB due to error(s) to prevent potential crash in libsmi. Module's conformance level: 1. See details at: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=560325"</p><p>Reading the linked page (bug tracker) it appears that this is a safeguard that is invoked if there are missing references in the MIB being parsed. But there doesn't appear to be any report (message or log file) that would lead me to what is missing.</p><p>The vendor MIB has external references to RFC1155-SMI, RFC1213-MIB, RFC-1212 and RFC-1215; I have explicitly loaded all of those (all were present in Wireshark's snmpmibs folder) and reloaded my vendor MIB, but the problem still persists.</p><p>FWIW I also get the same error for one of the standard MIBs that came with Wireshark (SNMPv2-SMI; this error seems to have been reported elsewhere; conceivably the same thing that is breaking the parsing of my vendor MIB could be breaking this too...</p><p>"Stopped processing module SNMPv2-SMI due to error(s) to prevent potential crash in libsmi. Module's conformance level: 1. See details at: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=560325"</p><p>BTW, the vendor MIB I am trying to import doesn't appear to have any syntax errors or other problems as it is working fine if loaded in Castle Rock SNMPc.</p><p>Anyone able to tell me how I can debug the MIB import so I can see where the thing is going wrong?</p><p>Thanks, Richard Culpan - Artevea Digital Ltd.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mib" rel="tag" title="see questions tagged &#39;mib&#39;">mib</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '10, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/6ad44cf78ec75a71621dd9ed002af306?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Culpan&#39;s gravatar image" /><p><span>Richard Culpan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Culpan has no accepted answers">0%</span></p></div></div><div id="comments-container-507" class="comments-container"><span id="508"></span><div id="comment-508" class="comment"><div id="post-508-score" class="comment-score"></div><div class="comment-text"><p>See the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bug Database</a>, especially <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5112">bug 5112</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5171">bug 5171</a></p></div><div id="comment-508-info" class="comment-info"><span class="comment-age">(14 Oct '10, 06:13)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-507" class="comment-tools"></div><div class="clear"></div><div id="comment-507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="509"></span>

<div id="answer-container-509" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-509-score" class="post-score" title="current number of votes">1</div><span id="post-509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Richard Culpan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>MIBs and SNMP are tricky protocols. Even though the Agent may be fine with it, libsmi may have a problem with it. Once it does it has nodes in non-finalized state in its tree, which can cause even crashes. To prevent that from happening MIBs are rejected when libsmi can't properly load them.</p><p>You should try to use smilint and see what it reports on your MIB. There's an online version available through the <a href="http://www.ibr.cs.tu-bs.de/projects/libsmi/index.html">libsmi website</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '10, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-509" class="comments-container"><span id="514"></span><div id="comment-514" class="comment"><div id="post-514-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply - I have used online version of "smilint"; it reported quite a lot of minor errors/warnings (mostly level 3), so I'm now analysing the report to see how I can improve the MIB and hopefully find which of the things found is tripping up the import into Wireshark.</p><p>Regards, Richard</p></div><div id="comment-514-info" class="comment-info"><span class="comment-age">(15 Oct '10, 02:33)</span> <span class="comment-user userinfo">Richard Culpan</span></div></div></div><div id="comment-tools-509" class="comment-tools"></div><div class="clear"></div><div id="comment-509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="515"></span>

<div id="answer-container-515" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-515-score" class="post-score" title="current number of votes">0</div><span id="post-515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For reference - after analysing the output of "smilint":</p><p>libsmi appears not to like (and chokes on) object identifiers that either:</p><ol><li>Starts in an upper case letter ("smilint" reports this as a "level 1" error (<em>must be fixed</em>) yet other programs such as Castle Rock SNMPc do not complain. So IMO it is really a "level 2" error (ignored by some implentations).</li><li>Is composed entirely of upper case letters ("smilint" reports a "level 1" error (internal - other error in libsmi) and aborts processing of the entire statement.</li></ol><p>To fix the errors I have renamed the offending objects such that they now begin with a lower case letter; the MIB now loads successfully in Wireshark.</p><p>Regards, Richard</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '10, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/6ad44cf78ec75a71621dd9ed002af306?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Culpan&#39;s gravatar image" /><p><span>Richard Culpan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Culpan has no accepted answers">0%</span></p></div></div><div id="comments-container-515" class="comments-container"></div><div id="comment-tools-515" class="comment-tools"></div><div class="clear"></div><div id="comment-515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

