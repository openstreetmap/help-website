+++
type = "question"
title = "can  wireshark disable 61850SMV dissector by user?"
description = '''as the title. i want to make wireshark1.5.1(or new vertion) dissects 61850SMV as wireshark1.2.9 remaining hex packets. can it done through settting something on wiresahrk interface?  how to set parameters of tshark in commondline to disable 61850SMV dissector?'''
date = "2011-09-16T02:46:00Z"
lastmod = "2011-09-20T07:58:00Z"
weight = 6413
keywords = [ "disable", "dissector" ]
aliases = [ "/questions/6413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can wireshark disable 61850SMV dissector by user?](/questions/6413/can-wireshark-disable-61850smv-dissector-by-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6413-score" class="post-score" title="current number of votes">0</div><span id="post-6413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>as the title.</p><p>i want to make wireshark1.5.1(or new vertion) dissects 61850SMV as wireshark1.2.9 remaining hex packets.</p><p>can it done through settting something on wiresahrk interface?</p><p>how to set parameters of tshark in commondline to disable 61850SMV dissector?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '11, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p><span>ylda_ljm0620</span><br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '11, 06:07</strong> </span></p></div></div><div id="comments-container-6413" class="comments-container"></div><div id="comment-tools-6413" class="comment-tools"></div><div class="clear"></div><div id="comment-6413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6465"></span>

<div id="answer-container-6465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6465-score" class="post-score" title="current number of votes">0</div><span id="post-6465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to disable a dissector you can either hardcode it and make changes in Makefile.common(epan/dissector) and CMakelist.tx(epan)...to remove the protocol completely ...else use the wireshark GTK menu&gt;protocols and uncheck the protocol which is registered</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '11, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6465" class="comments-container"></div><div id="comment-tools-6465" class="comment-tools"></div><div class="clear"></div><div id="comment-6465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

