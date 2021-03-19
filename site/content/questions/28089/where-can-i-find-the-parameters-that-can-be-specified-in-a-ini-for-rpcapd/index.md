+++
type = "question"
title = "Where can I find the parameters that can be specified in a .Ini for RPCAPD?"
description = '''I am attempting to use rpcapd &amp;amp; wireshark to gather some data remotely. I have been able to use the parameters displayed using the -h parameter from the command line. But I have not been able to locate the parameters and their syntax for use in a .ini file specified using the -f parameter.  I ha...'''
date = "2013-12-13T11:51:00Z"
lastmod = "2013-12-15T10:55:00Z"
weight = 28089
keywords = [ "rpcapd", "ini", "parameters" ]
aliases = [ "/questions/28089" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where can I find the parameters that can be specified in a .Ini for RPCAPD?](/questions/28089/where-can-i-find-the-parameters-that-can-be-specified-in-a-ini-for-rpcapd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28089-score" class="post-score" title="current number of votes">0</div><span id="post-28089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>I am attempting to use rpcapd &amp; wireshark to gather some data remotely.  I have been able to use the parameters displayed using the -h parameter from the command line.  But I have not been able to locate the parameters and their syntax for use in a .ini file specified using the -f parameter.

I have also tried using the -s parameter to &#39;save&#39; the currently running configuration, but It does not save all of the parameters needed to duplicate the configuration.
The only parameters I have been able to get saved are &#39;*PassiveClient*&#39; and &#39;*ActiveClient*&#39;.  Not other parameters specified on the command line are saved.

I have also tried using the parameters from the command line in the .ini file, They do not appear to work.</code></pre><p>Parameters I have seen:</p><p>Command line .Ini File -l PassiveClient -n NullAuthPermit -a ActiveCleint</p><p>I would like to find the .ini variants for the -4 and -p parameters at a minimum.<br />
</p><pre><code>I would also like to know if there is a way (and how) to use the *ID/Password* options or is Null Authentication the only option.  I see fields in wireShark to provide ID &amp; Pwd, But I have not been able to figure out how to set / use them.</code></pre><p>I am using WinPcap 4.1.3 and have tried this on Windows 7 (both 32 and 64 bit) with WireSharkVersion 1.10.3 (SVN Rev 53022 from /trunk-1.10).</p><p>Alan.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpcapd" rel="tag" title="see questions tagged &#39;rpcapd&#39;">rpcapd</span> <span class="post-tag tag-link-ini" rel="tag" title="see questions tagged &#39;ini&#39;">ini</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '13, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/c89893c29e1be2a892a4bbce28d53a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astrader&#39;s gravatar image" /><p><span>astrader</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astrader has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-28089" class="comments-container"></div><div id="comment-tools-28089" class="comment-tools"></div><div class="clear"></div><div id="comment-28089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28124"></span>

<div id="answer-container-28124" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28124-score" class="post-score" title="current number of votes">1</div><span id="post-28124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="astrader has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to find the .ini variants for the -4 and -p parameters at a minimum.</p></blockquote><p>According to the source code of WinPcap (fileconf.c), there are no supported parameters in the config file (.ini) other than: PassiveClient, ActiveClient and NullAuthPermit.</p><p>The rest of the options must be given as command line parameters.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28124" class="comments-container"></div><div id="comment-tools-28124" class="comment-tools"></div><div class="clear"></div><div id="comment-28124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

