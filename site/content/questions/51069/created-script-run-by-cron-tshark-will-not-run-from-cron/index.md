+++
type = "question"
title = "Created SCRIPT run by CRON, TSHARK will not run from CRON"
description = '''I have created a script to run tshark to get a packet capture periodically during the day on a REDHAT server. If I run the shell script under either &quot;root&quot; or another user id (MANUALLY) it works and writes to the files i&#x27;ve created. But if I let cron run the shell script, everything works except the...'''
date = "2016-03-21T09:44:00Z"
lastmod = "2016-03-21T14:19:00Z"
weight = 51069
keywords = [ "scheduled", "nonroot", "unpriviledged", "privileges" ]
aliases = [ "/questions/51069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Created SCRIPT run by CRON, TSHARK will not run from CRON](/questions/51069/created-script-run-by-cron-tshark-will-not-run-from-cron)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created a script to run tshark to get a packet capture periodically during the day on a REDHAT server. If I run the shell script under either "root" or another user id (MANUALLY) it works and writes to the files i've created. But if I let cron run the shell script, everything works except the " tshark -i eth1 -c # -w /tmp/<em>BUILD</em> ". I have tried changing permission on script, created files, binary file,... but nothing seems to allow tshark to run if script is executed via cron.</p><p>I also followed <a href="https://access.redhat.com/solutions/131583">link text</a> for TCPDUMP and WIRESHARK and neither have worked...</p><p>Any suggestions?? I know it is permissions related somewhere. should I make some kind of "cron" user id or group the owner of the script or tshark binary?</p><p>Thanks!!!!</p></div><div id="question-tags" class="tags-container tags">scheduled nonroot unpriviledged privileges</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '16, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div></div><div id="comments-container-51069" class="comments-container"></div><div id="comment-tools-51069" class="comment-tools"></div><div class="clear"></div><div id="comment-51069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51077"></span>

<div id="answer-container-51077" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51077-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the script runs successfully when ran manually from any user, it is not likely to be an issue of rights - a crontab is normally defined for a particular user and executes the commands with privileges of that user. I expect that your problem is that cron does not set the environment variables, including path. Therefore, you have to use absolute paths to the executables in the scripts started by cron. So instead of just <code>tshark</code>, you must use something like <code>/usr/bin/tshark</code>, but better use <code>which tshark</code> to find out what the absolute path really is at your Linux distribution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '16, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51077" class="comments-container"><span id="51079"></span><div id="comment-51079" class="comment"><div id="post-51079-score" class="comment-score"></div><div class="comment-text"><p>This makes sooo much sense and I will let you know the results once I test this.</p><p>Thank you!!!</p></div><div id="comment-51079-info" class="comment-info"><span class="comment-age">(21 Mar '16, 15:08)</span> msmorten</div></div><span id="51264"></span><div id="comment-51264" class="comment"><div id="post-51264-score" class="comment-score"></div><div class="comment-text"><p>Absolutely worked</p></div><div id="comment-51264-info" class="comment-info"><span class="comment-age">(29 Mar '16, 11:34)</span> msmorten</div></div></div><div id="comment-tools-51077" class="comment-tools"></div><div class="clear"></div><div id="comment-51077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

