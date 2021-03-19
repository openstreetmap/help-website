+++
type = "question"
title = "Getting list of interfaces - problem"
description = '''Hi, i have a problem with versions 1.6.11 and 1.8.3, i am trying to get the list of the interfaces and instead of getting the list to standard output, i get it on the std error. I don&#x27;t have this error on version 1.4.1 and it is works with the same code. Thanks My code:   ProcessStartInfo startInfo ...'''
date = "2012-11-19T02:08:00Z"
lastmod = "2012-11-19T10:25:00Z"
weight = 16042
keywords = [ "interfaces" ]
aliases = [ "/questions/16042" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting list of interfaces - problem](/questions/16042/getting-list-of-interfaces-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16042-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have a problem with versions 1.6.11 and 1.8.3, i am trying to get the list of the interfaces and instead of getting the list to standard output, i get it on the std error. I don't have this error on version 1.4.1 and it is works with the same code. Thanks My code:</p><pre><code>    ProcessStartInfo startInfo = new ProcessStartInfo(m_sTsharkPath);
    startInfo.Arguments = &quot;-D&quot;;

    startInfo.RedirectStandardError = true;
    startInfo.RedirectStandardOutput = true;
    startInfo.UseShellExecute = false;
    startInfo.CreateNoWindow = true;

    Process p = Process.Start(startInfo);

    String output = p.StandardOutput.ReadToEnd();
    String error = p.StandardError.ReadToEnd();

    p.WaitForExit(waitingTime);</code></pre></div><div id="question-tags" class="tags-container tags">interfaces</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '12, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/06f50401080384cf406ae8798bb821e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaa&#39;s gravatar image" /><p>aaa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaa has no accepted answers">0%</span></p></div></div><div id="comments-container-16042" class="comments-container"></div><div id="comment-tools-16042" class="comment-tools"></div><div class="clear"></div><div id="comment-16042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16070"></span>

<div id="answer-container-16070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16070-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it would appear that Wireshark was intentionally changed to send this output to stderr; the change came in <a href="https://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=36387">revision 36387</a>. Apparently it was necessary for "-D" to work on Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16070" class="comments-container"></div><div id="comment-tools-16070" class="comment-tools"></div><div class="clear"></div><div id="comment-16070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

