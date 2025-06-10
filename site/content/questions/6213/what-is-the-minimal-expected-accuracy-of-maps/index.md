+++
type = "question"
title = "What is the minimal expected accuracy of maps?"
description = '''For example in this view the road that ends in the middle of the woods (tile) does not really end there, but goes to the village and connects to the main road near the pond (tile).  I am sure it is there and how it looks, but I cannot draw it precisely without GPS trace. Should I draw it as a straig...'''
date = "2011-07-08T00:06:00Z"
lastmod = "2011-07-09T23:31:00Z"
weight = 6213
keywords = [ "quality", "accuracy" ]
aliases = [ "/questions/6213" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [What is the minimal expected accuracy of maps?](/questions/6213/what-is-the-minimal-expected-accuracy-of-maps)

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
<span id="post-6213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6213-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example in <a href="http://www.openstreetmap.org/?lat=49.64404&amp;lon=15.44478&amp;zoom=16&amp;layers=M">this</a> view the road that ends in the middle of the woods (<a href="http://c.tile.openstreetmap.org/16/35580/22327.png">tile</a>) does not really end there, but goes to the village and connects to the main road near the pond (<a href="http://a.tile.openstreetmap.org/16/35578/22325.png">tile</a>).</p>
<p>I am sure it is there and how it looks, but I cannot draw it precisely without GPS trace. Should I draw it as a straight line and correct later? There is valuable information added (points are connected and that is the important part for navigation).</p>
<p>And how about GPS traces with limited accuracy?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quality" rel="tag" title="see questions tagged &#39;quality&#39;">quality</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '11, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-6213" class="comments-container">
&#10;</div>
<div id="comment-tools-6213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6213-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="6249"></span>

<div id="answer-container-6249" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6249-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-6249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Regarding the "general question" of minimum expected accuracy - I'd tend to expect that any edit should leave a map that is overall more accurate than it had been before the change was made.</p>
<p>In this case, a section of road is/was completely missing, so anything that indicates the presence of the road is improving the overall accuracy of the map.</p>
<p>Where the accuracy is substantially different from then level of accuracy of surrounding objects, I'd expect a fixme= tag, but if a significant number of ways in an area are approximate, the source= tag should be sufficient.</p>
<p>That then leaves open the question of how to properly determine the accuracy of the surrounding data when adding data that you can't tell whether it's more or less accurate than what's already there, but discussion of that would belong in another venue...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '11, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/b95e1b5cb818be577b5561688a50368c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banoffee&#39;s gravatar image" />
<p><span>banoffee</span><br />
<span class="score" title="884 reputation points">884</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="banoffee has 3 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6249" class="comments-container">
<span id="6260"></span>
<div id="comment-6260" class="comment">
<div id="post-6260-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Improved accuracy of map after edit seems like an easy-to-follow policy.</p>
</div>
<div id="comment-6260-info" class="comment-info">
<span class="comment-age">(09 Jul '11, 23:31)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-6249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6249-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6221"></span>

<div id="answer-container-6221" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6221-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-6221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Feel free to "guess" the road in your case, and revisit the geometry when you have better sources available.</p>
<p>But I would add a caution to this - a couple of years ago someone added straight line connections between railway stations across a country in Europe. This was completely inappropriate given that these cut straight through areas where the roads were already well mapped.</p>
<p>Instead, I would say the "minimal expected accuracy" should be based on the existing accuracy, and the density of real-world features, of the surrounding area. So a straight line through a forest might be appropriate where a straight line though an urban area is not, and a straight line through an unmapped area may be appropriate where a straight line through a carefully mapped area is not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '11, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-6221" class="comments-container">
<span id="6233"></span>
<div id="comment-6233" class="comment">
<div id="post-6233-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We had a similar discussion in France about subway mapping in Paris. Some people mapped underground features very approximately (no GPS, no aerial imagery, just personnal feeling) where everything on the ground and above is very, very accurate (cadastre, aerial imagery).</p>
</div>
<div id="comment-6233-info" class="comment-info">
<span class="comment-age">(08 Jul '11, 15:40)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-6221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6221-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6214"></span>

<div id="answer-container-6214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6214-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-6214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would not hesitate to "guess" the road in your case. You are right in saying that the topological information (what connects to what) is more important than the geometry. You can always add <code>source=interpolation</code>, or a note tag saying you guessed it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '11, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '11, 14:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-6214" class="comments-container">
&#10;</div>
<div id="comment-tools-6214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6225"></span>

<div id="answer-container-6225" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6225-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-6225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you do add the roads, make sure to use a 'FIXME' tag. For example, 'fixme=Approximate route, needs survey'. Several mapping tools will highlight such 'fixme's and alert nearby mappers that the road needs improving.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '11, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-6225" class="comments-container">
<span id="6228"></span>
<div id="comment-6228" class="comment">
<div id="post-6228-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>... or even more concisely "fixme=resurvey", as suggested at <a href="http://wiki.openstreetmap.org/wiki/Fixme">http://wiki.openstreetmap.org/wiki/Fixme</a> and widely used.</p>
</div>
<div id="comment-6228-info" class="comment-info">
<span class="comment-age">(08 Jul '11, 13:55)</span> <span class="comment-user userinfo">banoffee</span>
</div>
</div>
</div>
<div id="comment-tools-6225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6225-form-container" class="comment-form-container">
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

