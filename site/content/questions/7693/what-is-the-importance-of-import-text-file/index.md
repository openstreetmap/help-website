+++
type = "question"
title = "What is the Importance of Import Text File?"
description = '''If I Import any file either text or pcap, I cannot see any packets on the window but while closing Wireshark asks for saving the file. What is the Use of this Import option? Why cannot we see the packets? '''
date = "2011-11-28T23:19:00Z"
lastmod = "2011-11-29T14:44:00Z"
weight = 7693
keywords = [ "import" ]
aliases = [ "/questions/7693" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the Importance of Import Text File?](/questions/7693/what-is-the-importance-of-import-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7693-score" class="post-score" title="current number of votes">0</div><span id="post-7693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I Import any file either text or pcap, I cannot see any packets on the window but while closing Wireshark asks for saving the file. What is the Use of this Import option? Why cannot we see the packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '11, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div></div><div id="comments-container-7693" class="comments-container"><span id="7712"></span><div id="comment-7712" class="comment"><div id="post-7712-score" class="comment-score"></div><div class="comment-text"><p>There's no option to "import" a pcap file. The "Import" function expects the file to be a text file; if it's not - and pcap files aren't text - you won't see any packets, as Jaap indicated. If you have a pcap file, you just open it; you don't import it.</p></div><div id="comment-7712-info" class="comment-info"><span class="comment-age">(29 Nov '11, 14:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7693" class="comment-tools"></div><div class="clear"></div><div id="comment-7693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7696"></span>

<div id="answer-container-7696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7696-score" class="post-score" title="current number of votes">0</div><span id="post-7696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Import can be used for specifically formatted text files, see section 5.5 of the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html">Users Guide</a>. When starting an import an empty capture file is created, which is subsequently filled with imported packets. If the import fails to read any valid packet data all that remains is an opened, but empty capture file. This has to be closed/saved when closing Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '11, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7696" class="comments-container"></div><div id="comment-tools-7696" class="comment-tools"></div><div class="clear"></div><div id="comment-7696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

