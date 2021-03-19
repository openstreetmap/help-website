+++
type = "question"
title = "How to compare old plugin performance with updated one?"
description = '''I have updated an old plugin(Version 1.6) to Version 2.2. I have to show that, the new plugin performas and Shows exactly the same data as the old one(for some certain PCAP files). How can I show this? It is impossible to manually show the comparison.'''
date = "2017-02-28T07:53:00Z"
lastmod = "2017-02-28T09:18:00Z"
weight = 59731
keywords = [ "comparison", "dissector", "update", "updateplugin", "plugin" ]
aliases = [ "/questions/59731" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to compare old plugin performance with updated one?](/questions/59731/how-to-compare-old-plugin-performance-with-updated-one)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59731-score" class="post-score" title="current number of votes">0</div><span id="post-59731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have updated an old plugin(Version 1.6) to Version 2.2. I have to show that, the new plugin performas and Shows exactly the same data as the old one(for some certain PCAP files). How can I show this? It is impossible to manually show the comparison.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-comparison" rel="tag" title="see questions tagged &#39;comparison&#39;">comparison</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-updateplugin" rel="tag" title="see questions tagged &#39;updateplugin&#39;">updateplugin</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-59731" class="comments-container"></div><div id="comment-tools-59731" class="comment-tools"></div><div class="clear"></div><div id="comment-59731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59735"></span>

<div id="answer-container-59735" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59735-score" class="post-score" title="current number of votes">1</div><span id="post-59735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xaheen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use tshark to output to a text file and compare old and new. Using the <code>-T fields -e fieldname1 -e fieldname2 -e ...</code> options you can select particular fields of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '17, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59735" class="comments-container"><span id="59738"></span><div id="comment-59738" class="comment"><div id="post-59738-score" class="comment-score"></div><div class="comment-text"><p>Thanks a loit :)</p></div><div id="comment-59738-info" class="comment-info"><span class="comment-age">(28 Feb '17, 09:18)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-59735" class="comment-tools"></div><div class="clear"></div><div id="comment-59735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

