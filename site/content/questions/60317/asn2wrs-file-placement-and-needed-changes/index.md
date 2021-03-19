+++
type = "question"
title = "Asn2Wrs file placement and needed changes?"
description = '''Hey there, I&#x27;ve tried building an asn2wrs dissector but I can&#x27;t find any up to date resource. README.dissector, README.plugins and the web docs don&#x27;t seem to mention that while the Asn2wrs wiki entry is from 2010. A small guide or a few pointers would be much appreciated, best regards.'''
date = "2017-03-24T09:09:00Z"
lastmod = "2017-03-30T06:58:00Z"
weight = 60317
keywords = [ "asn2wrs", "build" ]
aliases = [ "/questions/60317" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Asn2Wrs file placement and needed changes?](/questions/60317/asn2wrs-file-placement-and-needed-changes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60317-score" class="post-score" title="current number of votes">0</div><span id="post-60317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there, I've tried building an asn2wrs dissector but I can't find any up to date resource. README.dissector, README.plugins and the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/index.html">web docs</a> don't seem to mention that while the <a href="https://wiki.wireshark.org/Asn2wrs">Asn2wrs wiki entry</a> is from 2010.</p><p>A small guide or a few pointers would be much appreciated, best regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn2wrs" rel="tag" title="see questions tagged &#39;asn2wrs&#39;">asn2wrs</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '17, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/0033a89e1e79ac90094a195fb76b211b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clem&#39;s gravatar image" /><p><span>clem</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clem has one accepted answer">100%</span></p></div></div><div id="comments-container-60317" class="comments-container"></div><div id="comment-tools-60317" class="comment-tools"></div><div class="clear"></div><div id="comment-60317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60334"></span>

<div id="answer-container-60334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60334-score" class="post-score" title="current number of votes">0</div><span id="post-60334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On what OS are you building? If you are adding a new dissector add a new dir in /epan/dissectors/asn1 and add your files there. Then just compare with an existing dissector and add similar stuff for your new one. If building with cmake add your dissector and the build files run cmake then in the build dir do (h248 as an example)</p><p>On Windows, you need to go to epan\dissectors\asn\h248 folder and run: msbuild /m /p:Configuration=RelWithDebInfo generate_dissector-h248.vcxproj</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '17, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-60334" class="comments-container"><span id="60440"></span><div id="comment-60440" class="comment"><div id="post-60440-score" class="comment-score"></div><div class="comment-text"><p>Building on ubuntu 16, tried make didn't get that to work so far. Using cmake I got to the point of invoking asn2wrs and now I'm also getting compile errors, which are probably due to the antique example files. Progress.</p><p>To get to this point I've done the following:</p><ul><li>create 'foo' dir in ws/epan/dissectors/asn1/</li><li>copied and changed the required files from h248</li><li>in main-dir create CMakeListsCustom.txt, add "epan/dissectors/asn1/foo" to CUSTOM_PLUGIN_SRC_DIR (invokes asn2wrs ?)</li><li>ws/epan/dissectors/CMakeListsCustom.txt added "packet-foo.c" to CUSTOM_DISSECTOR_SRC (invokes compile ?)</li></ul><p>Is there a way to compile asn2wrs-dissector as plugins or this not an intended ?</p></div><div id="comment-60440-info" class="comment-info"><span class="comment-age">(30 Mar '17, 06:58)</span> <span class="comment-user userinfo">clem</span></div></div></div><div id="comment-tools-60334" class="comment-tools"></div><div class="clear"></div><div id="comment-60334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

