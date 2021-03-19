+++
type = "question"
title = "tshark -T ek or JSON export in a development version"
description = '''Hi guys I&#x27;m deploying a dev version of Wireshark on Ubuntu, I&#x27;m using a SAP dissector plugin for this version.  I wanted to use tshark to convert some pcaps into EK JSON format. but it seems that the version does not support -T ek nor JSON export.  the question is: is there any possibility to upgrad...'''
date = "2016-11-21T04:54:00Z"
lastmod = "2016-11-21T06:08:00Z"
weight = 57519
keywords = [ "search", "json", "tshark", "elastic" ]
aliases = [ "/questions/57519" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -T ek or JSON export in a development version](/questions/57519/tshark-t-ek-or-json-export-in-a-development-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57519-score" class="post-score" title="current number of votes">0</div><span id="post-57519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys</p><p>I'm deploying a dev version of Wireshark on Ubuntu, I'm using a SAP dissector plugin for this version. I wanted to use tshark to convert some pcaps into EK JSON format. but it seems that the version does not support -T ek nor JSON export.</p><p>the question is: is there any possibility to upgrade the tshark for the current installation? also would this speical dissector be included in the EK export by default or will I need furher work within the Mapping?</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-elastic" rel="tag" title="see questions tagged &#39;elastic&#39;">elastic</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '16, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/7cce78d738fa16cbb8d95bb5699d8a66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zalabany&#39;s gravatar image" /><p><span>Zalabany</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zalabany has no accepted answers">0%</span></p></div></div><div id="comments-container-57519" class="comments-container"></div><div id="comment-tools-57519" class="comment-tools"></div><div class="clear"></div><div id="comment-57519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57523"></span>

<div id="answer-container-57523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57523-score" class="post-score" title="current number of votes">1</div><span id="post-57523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>if your tshark version does not support -T ek or -T json, it means that it is older than version 2.2.0 and cannot be considered anymore as a development version( current development versions are labeled 2.3.0). This can be double checked by running the following command</p><pre><code>tshark -v</code></pre><p>And check the version printed. Maybe you have a globally installed tshark version that takes precedence on your development one? Which version are you supposed to have installed?</p><p>The various output formats can be checked by running</p><pre><code>tshark -h</code></pre><p>If you compiled a version with EK/JSON output format support, you can run it from the build folder (and eventually making an alias). The following <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBinary.html">link</a> gives you some tips on how to generate a .deb installer from the source code but it might not be an easy task. If you want to upgrade, ensure to uninstall previous version first (you cannot upgrade tshark alone as it replies on some shared libraries that are in common with wireshark GUI).</p><p>Any dissector should be part of the EK output without any change as long as it is seen with any other output format (-T pdml for example).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '16, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-57523" class="comments-container"></div><div id="comment-tools-57523" class="comment-tools"></div><div class="clear"></div><div id="comment-57523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

