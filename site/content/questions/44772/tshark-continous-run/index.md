+++
type = "question"
title = "tshark continous run"
description = '''Hi guys, Any help will be useful here. Im able to understand the camel flow however I still need to understand that If I can use tshark continously reading from the network card? There are 2 questions here: 1) Will tshark die after sometime due to memory problems? Although I read few topics here tha...'''
date = "2015-08-03T06:36:00Z"
lastmod = "2015-08-03T19:56:00Z"
weight = 44772
keywords = [ "tshark", "camel" ]
aliases = [ "/questions/44772" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark continous run](/questions/44772/tshark-continous-run)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44772-score" class="post-score" title="current number of votes">0</div><span id="post-44772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>Any help will be useful here. Im able to understand the camel flow however I still need to understand that If I can use tshark continously reading from the network card? There are 2 questions here:</p><p>1) Will tshark die after sometime due to memory problems? Although I read few topics here that said for some users tshark ran for months especially on TCAP and CAMEL protocols because tshark doesnt create any maps in memory for these protocols.</p><p>2) Will tshark be fast enough to read all packets from network card? There will be very high traffic on my application server because all call data for the operator are mirrored on this server.</p><p>Im using the following command to capture data, with input file (-r) its too slow so Im worried about the performance when using with ehternet card.</p><p>tshark -Tpdml -Y "camel.InitialDPArg || (camel.EventReportBCSMArg &amp;&amp; (camel.eventTypeBCSM==4||camel.eventTypeBCSM==5))" -r "\home\usr0121\hcm.dump"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-camel" rel="tag" title="see questions tagged &#39;camel&#39;">camel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '15, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/80d70be65afb9b6b3bbeda33fb06e824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karan%20Grover&#39;s gravatar image" /><p><span>Karan Grover</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karan Grover has no accepted answers">0%</span></p></div></div><div id="comments-container-44772" class="comments-container"><span id="44804"></span><div id="comment-44804" class="comment"><div id="post-44804-score" class="comment-score"></div><div class="comment-text"><p>Is there a particular reason why you have chosen pdml as the format to print to the screen? I only ask because it might be that your terminal is having a difficult time keeping up with the large amount of text printed to the screen for each packet/frame you receive, as there is a lot of output per packet/frame with pdml.</p></div><div id="comment-44804-info" class="comment-info"><span class="comment-age">(03 Aug '15, 13:50)</span> <span class="comment-user userinfo">greenfreq</span></div></div><span id="44807"></span><div id="comment-44807" class="comment"><div id="post-44807-score" class="comment-score"></div><div class="comment-text"><p>You are right there is a lot of data but I redirect all of this to my java program tshark...... | java .... and I have chosen pdml because its easier for java code to parse it.</p></div><div id="comment-44807-info" class="comment-info"><span class="comment-age">(03 Aug '15, 19:56)</span> <span class="comment-user userinfo">Karan Grover</span></div></div></div><div id="comment-tools-44772" class="comment-tools"></div><div class="clear"></div><div id="comment-44772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

