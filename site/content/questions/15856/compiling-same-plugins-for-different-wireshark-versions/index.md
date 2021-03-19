+++
type = "question"
title = "Compiling same plugins for different Wireshark versions"
description = '''Hello, I have a Wireshark plugin here working properly for Wireshark 1.7. On Wireshark 1.8, I get some dissection errors. I know that plugins are usually not compatible with Wireshark versions they were not compiled for. So, I decided to recompile my plugin. I have a Linux system where the stuff is ...'''
date = "2012-11-13T02:25:00Z"
lastmod = "2012-11-15T02:43:00Z"
weight = 15856
keywords = [ "compile", "different", "complilation", "version", "plugin" ]
aliases = [ "/questions/15856" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Compiling same plugins for different Wireshark versions](/questions/15856/compiling-same-plugins-for-different-wireshark-versions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15856-score" class="post-score" title="current number of votes">0</div><span id="post-15856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a Wireshark plugin here working properly for Wireshark 1.7. On Wireshark 1.8, I get some dissection errors. I know that plugins are usually not compatible with Wireshark versions they were not compiled for. So, I decided to recompile my plugin. I have a Linux system where the stuff is supposed to run. Now, what does it exactly mean to compile the plugin for another version of Wireshark? What changes are actually required? Is it about changing the source code itself or about changing the environment somehow, or both?</p><p>Kind regards Ewgenij</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-different" rel="tag" title="see questions tagged &#39;different&#39;">different</span> <span class="post-tag tag-link-complilation" rel="tag" title="see questions tagged &#39;complilation&#39;">complilation</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '12, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-15856" class="comments-container"></div><div id="comment-tools-15856" class="comment-tools"></div><div class="clear"></div><div id="comment-15856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15862"></span>

<div id="answer-container-15862" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15862-score" class="post-score" title="current number of votes">1</div><span id="post-15862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ewgenijkkg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to put your plugin sources in the source tree of 1.8 and recompile, if the API has changed that recompilation may fail and you need to update the API.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '12, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-15862" class="comments-container"><span id="15926"></span><div id="comment-15926" class="comment"><div id="post-15926-score" class="comment-score"></div><div class="comment-text"><p>So, the only thing I have to do is to put my plugin folder to wireshark/plugins and execute make inside my plugin folder. And if it would not output any errors then I'm finished. Right? :)</p></div><div id="comment-15926-info" class="comment-info"><span class="comment-age">(15 Nov '12, 02:43)</span> <span class="comment-user userinfo">Ewgenijkkg</span></div></div></div><div id="comment-tools-15862" class="comment-tools"></div><div class="clear"></div><div id="comment-15862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15863"></span>

<div id="answer-container-15863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15863-score" class="post-score" title="current number of votes">1</div><span id="post-15863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you keep in mind that plugins are compiled against the EPAN dissector interface and uses the EPAN header files several changes come to mind:</p><ul><li>changed / new function signatures</li><li>changed types / enums</li></ul><p>Therefore porting your plugin source requires a new build environment and, depending on the functions / types used, changes to your source code. There's no delta document listing these changes, watch your compiler output for hints.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '12, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15863" class="comments-container"></div><div id="comment-tools-15863" class="comment-tools"></div><div class="clear"></div><div id="comment-15863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

