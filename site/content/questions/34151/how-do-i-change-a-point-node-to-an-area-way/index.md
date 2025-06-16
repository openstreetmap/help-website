+++
type = "question"
title = "How do I change a point (node) to an area (way)?"
description = '''A related question to this one ... I created a point to represent a cafe. Now, I want to go back and create an area so that I can mark the whole building as housing that cafe. How should I do this, without losing all the details I put into the point (address, internet access, website, etc.)? I tried...'''
date = "2014-06-19T21:00:00Z"
lastmod = "2014-06-28T01:05:00Z"
weight = 34151
keywords = [ "node", "editing", "way", "area" ]
aliases = [ "/questions/34151" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I change a point (node) to an area (way)?](/questions/34151/how-do-i-change-a-point-node-to-an-area-way)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34151-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A related question to <a href="/questions/27594/can-you-change-a-closed-line-into-an-area">this one</a> ...</p>
<p>I created a point to represent a cafe. Now, I want to go back and create an area so that I can mark the whole building as housing that cafe.</p>
<p>How should I do this, without losing all the details I put into the point (address, internet access, website, etc.)?</p>
<p>I tried adding a tag "building=yes" but that didn't immediately allow me to "draw" the building's outline.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '14, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/92c443d5ff9cd4d637081fa65be3335d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="borbash&#39;s gravatar image" />
<p><span>borbash</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="borbash has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '14, 01:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-34151" class="comments-container">
&#10;</div>
<div id="comment-tools-34151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34151-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="34155"></span>

<div id="answer-container-34155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34155-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-34155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Potlatch 2, you can click on the node, then Shift-click, and it will turn the node into a rectangular way with all the tags intact.</p>
<p>If you only want to transfer the tags from existing node to existing way and leave the node intact, you could first transfer the tags to another node, then create that into an way, then copy the tags from that way to the existing one. Stepwise:</p>
<ol>
<li>Click on existing node with tags</li>
<li>Create new node</li>
<li>Press R while on new node to transfer tags from existing node to new node</li>
<li>Shift-click to create new way from new node</li>
<li>Click on existing way</li>
<li>Press R to transfer tags from new way to existing way</li>
<li>Delete new way</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '14, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-34155" class="comments-container">
&#10;</div>
<div id="comment-tools-34155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34155-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34152"></span>

<div id="answer-container-34152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34152-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This really depends on the editor you are using, which you don't mention. In JOSM you can copy the tags of any object to a new one (Ctrl+Shift+V), in other editors it may not be possible. I currently don't know of any editor that allows you to "expand" a node in to a way, so typically you will draw a new polygon/area and copy the tags to that, worst case one by one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '14, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '14, 04:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span></p>
</div>
</div>
<div id="comments-container-34152" class="comments-container">
<span id="34154"></span>
<div id="comment-34154" class="comment">
<div id="post-34154-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I used the iD editor. I find it easy to use, since it runs right in the browser, not as a separate application.</p>
</div>
<div id="comment-34154-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 21:15)</span> <span class="comment-user userinfo">borbash</span>
</div>
</div>
<span id="34159"></span>
<div id="comment-34159" class="comment">
<div id="post-34159-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@borbash</span>: "Easy to use" ... or not. Use <span>JOSM</span>. Your requested operation is sooo easy and clear there.</p>
</div>
<div id="comment-34159-info" class="comment-info">
<span class="comment-age">(20 Jun '14, 00:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="34384"></span>
<div id="comment-34384" class="comment">
<div id="post-34384-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK @ aseerel4c26 @ SimonPoole I have downloaded JOSM and downloaded OSM data into it for this neighborhood. I have selected the cafe (which is a point and I want to make it an area) and I can see its nine tags when in JOSM I click on the "tag" icon at left.</p>
<p>in JOSM How can I make this from a point to an area? In the tag popup there are not only the nine tags for the point, but five things listed above the tags, "Facilities...", "Man Made...", "Annotation..." etc.</p>
</div>
<div id="comment-34384-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 18:57)</span> <span class="comment-user userinfo">borbash</span>
</div>
</div>
</div>
<div id="comment-tools-34152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34386"></span>

<div id="answer-container-34386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34386-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>not sure what you mean by this "In the tag popup there are not only the nine tags for the point, but five things listed above the tags, "Facilities...", "Man Made...", "Annotation..." etc."</p>
<p>But here is how I would do it using JOSM:<br />
draw the outline of the cafe using the node drawing tool,<br />
click off (select the select tool and click on the background ie not on an object),<br />
select your node with all the tags on using the select tool, select Edit, Copy from the top menu,<br />
select the new building outline you drew and select Edit, Paste Tags from the top menu,<br />
check tags seem suitable, select your old node and delete.<br />
Probably best to read the Help in JOSM to get familiar with this editor first.<br />
I found the most important think I needed to know was to "click off" after doing each object draw.<br />
<img src="/upfiles/select.png" alt="tools" /></p>
<p>It is also very helpful to tick Layers and Tags/Memberships under the Windows menu and place these at the right side where you can see them. You can add tags there or from the Presets menu. You add the Bing imagery from the Imagery menu and you will see all the layers you have loaded in the box at the right.<br />
</p>
<p><img src="/upfiles/layers.png" alt="layers" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '14, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '14, 20:57</strong> </span></p>
</div>
</div>
<div id="comments-container-34386" class="comments-container">
<span id="34389"></span>
<div id="comment-34389" class="comment">
<div id="post-34389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Almost there. I have created the outline of the building but JOSM warns that it is not a closed way (area) but just a Way. How do I close the way? (I did spend time looking for the answer before posting.)</p>
</div>
<div id="comment-34389-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 21:26)</span> <span class="comment-user userinfo">borbash</span>
</div>
</div>
<span id="34390"></span>
<div id="comment-34390" class="comment">
<div id="post-34390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Not a closed way" means the end node doesn't <em>quite</em> join the start node. Zoom in a bit and you should be able to see the problem.</p>
</div>
<div id="comment-34390-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 21:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34391"></span>
<div id="comment-34391" class="comment">
<div id="post-34391-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try a double-click on the last node to join it to the first node to complete the building. If you zoom in and see 2 nodes close together instead of over each, select both and 'merge selection' from the edit menu. A building has to be a closed polygon - it can not have an open side.</p>
</div>
<div id="comment-34391-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 21:44)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="34393"></span>
<div id="comment-34393" class="comment">
<div id="post-34393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@borbash</span>: very good! The wiki would tell you what a <span>closed way</span> is. Select the way (and its last node if the last node is a shared node), go into add mode (key A), and then click on the first node.</p>
</div>
<div id="comment-34393-info" class="comment-info">
<span class="comment-age">(28 Jun '14, 01:05)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34386-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

