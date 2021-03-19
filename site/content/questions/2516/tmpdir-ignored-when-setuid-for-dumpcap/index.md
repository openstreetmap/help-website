+++
type = "question"
title = "TMPDIR ignored when setuid for dumpcap"
description = '''Hi,  trying to get rid of &quot;sudo&quot;, I&#x27;ve set setuid for &quot;root&quot; user on dumpcap. (SLES 10.3) It&#x27;s working fine with regard to capturing. However, the TMPDIR variable is ignored. Is this a security feature? Does somebody know, how to circumvent this? Best regards Philipp'''
date = "2011-02-23T05:25:00Z"
lastmod = "2012-02-29T07:43:00Z"
weight = 2516
keywords = [ "setuid", "dumpcap", "tmpdir" ]
aliases = [ "/questions/2516" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TMPDIR ignored when setuid for dumpcap](/questions/2516/tmpdir-ignored-when-setuid-for-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2516-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>trying to get rid of "sudo", I've set setuid for "root" user on dumpcap. (SLES 10.3)</p><p>It's working fine with regard to capturing. However, the TMPDIR variable is ignored.</p><p>Is this a security feature? Does somebody know, how to circumvent this?</p><p>Best regards Philipp</p></div><div id="question-tags" class="tags-container tags">setuid dumpcap tmpdir</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '11, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/c51791d484acc40bc9a3bb13563ad643?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvh&#39;s gravatar image" /><p>pvh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Feb '11, 05:26</p></div></div><div id="comments-container-2516" class="comments-container"></div><div id="comment-tools-2516" class="comment-tools"></div><div class="clear"></div><div id="comment-2516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9279"></span>

<div id="answer-container-9279" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9279-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is, apparently, a glibc feature. See:</p><p><a href="https://bugzilla.redhat.com/show_bug.cgi?id=129682#c1">https://bugzilla.redhat.com/show_bug.cgi?id=129682#c1</a></p><p>and/or:</p><p><a href="http://lists.gnu.org/archive/html/bug-glibc/2003-08/msg00076.html">http://lists.gnu.org/archive/html/bug-glibc/2003-08/msg00076.html</a></p><p>Oh, and I can't think of a way to avoid it.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Feb '12, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 06:59</p></div></div><div id="comments-container-9279" class="comments-container"><span id="9287"></span><div id="comment-9287" class="comment"><div id="post-9287-score" class="comment-score"></div><div class="comment-text"><p>In fact, it's probably a feature of many UN\*Xes other than Linux distributions with glibc; environment variables are often ignored by programs and library routines when running set-UID, as they can be maliciously set in an attempt to trick the set-UID program into reading from or writing to files to which the user shouldn't be given access.</p><p>And, as such, there is no way to disable that feature. See, however, <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">the Wireshark Wiki page on capture privileges</a> for some information on how to give dumpcap sufficient privileges.</p></div><div id="comment-9287-info" class="comment-info"><span class="comment-age">(29 Feb '12, 23:45)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9279" class="comment-tools"></div><div class="clear"></div><div id="comment-9279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

