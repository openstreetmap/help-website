+++
type = "question"
title = "How to dump conv,ip every 1 ~ 10 milliseconds?"
description = '''I know that with the -z io,stat,0.01 you can specify seconds as intervals, but what I want to do is list conv,ip every 1 ~ 10 milliseconds. tshark -q -r Test.pcapng -z conv,ip will give me all conversations but that&#x27;s for a 34MByte file. I would hate to have to use editcap to break this 34MB file up...'''
date = "2017-03-13T23:24:00Z"
lastmod = "2017-03-13T23:24:00Z"
weight = 60047
keywords = [ "with", "ip", "command", "conv", "tick_interval" ]
aliases = [ "/questions/60047" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dump conv,ip every 1 ~ 10 milliseconds?](/questions/60047/how-to-dump-convip-every-1-10-milliseconds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60047-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know that with the -z io,stat,0.01 you can specify seconds as intervals, but what I want to do is list conv,ip every 1 ~ 10 milliseconds.</p><p>tshark -q -r Test.pcapng -z conv,ip will give me all conversations but that's for a 34MByte file. I would hate to have to use editcap to break this 34MB file up into oodles of 1 ~ 10msec files and then run this command on all the oodles of files, but I find no way to specify start and stop time using tshark!</p><p>Any recommendations?</p><p>How about modifying/adding a new variable to the conv,ip command to like below: tshark -q -r Test.pcapng -z conv,ip,0.010 (dump conv,ip every 10 msecs) tshark -q -r Test.pcapng -z conv,ip,0.001 (dump conv,ip every msec)</p><p>Cheers,</p></div><div id="question-tags" class="tags-container tags">with ip command conv tick_interval</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '17, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p>wbenton<br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-60047" class="comments-container"></div><div id="comment-tools-60047" class="comment-tools"></div><div class="clear"></div><div id="comment-60047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

