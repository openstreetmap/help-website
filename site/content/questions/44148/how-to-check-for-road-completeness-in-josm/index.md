+++
type = "question"
title = "How to check for road completeness in JOSM?"
description = '''I have found a validation test at https://wiki.openstreetmap.org/wiki/JOSM/Validator called incomplete ways which is exactly what I&#x27;m looking for to use in JOSM. However, in JOSM this validator/test does not exist. How can I find the validator or how else can a search for ways that end with one node...'''
date = "2015-07-13T11:13:00Z"
lastmod = "2015-09-17T05:47:00Z"
weight = 44148
keywords = [ "josm", "validator" ]
aliases = [ "/questions/44148" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to check for road completeness in JOSM?](/questions/44148/how-to-check-for-road-completeness-in-josm)

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
<span id="post-44148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44148-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have found a validation test at <a href="https://wiki.openstreetmap.org/wiki/JOSM/Validator">https://wiki.openstreetmap.org/wiki/JOSM/Validator</a> called incomplete ways which is exactly what I'm looking for to use in JOSM. However, in JOSM this validator/test does not exist. How can I find the validator or how else can a search for ways that end with one node or less?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '15, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/19fd6c1499513907697c5821829c5e83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BmanS&#39;s gravatar image" />
<p><span>BmanS</span><br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BmanS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44148" class="comments-container">
&#10;</div>
<div id="comment-tools-44148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44148-form-container" class="comment-form-container">
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

<span id="44211"></span>

<div id="answer-container-44211" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44211-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-44211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible to specify a custom rule that will flag unconnected end nodes, here's a simple version:</p>
<pre><code>way[highway]&gt;[index=1] node!:connection,
way[highway]&gt;[index=-1] node!:connection{
    throwWarning: tr(&quot;Unconnected end node.&quot;);
}</code></pre>
<p>To use such a rule in JOSM, save the above in a file with a name like <code>my.validator.mapcss</code> and then add it to the active rules. Edit-&gt;Preferences, Select the Checkmark, select the "Tag checker rules" tab and then click the <code>+</code> button on the right:</p>
<p><img src="http://i.imgur.com/QqOzmmi.png" alt="Add validation ruleset" /></p>
<p><a href="https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">Take a look at the docs to see about making the rule more specific.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '15, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '15, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-44211" class="comments-container">
<span id="44583"></span>
<div id="comment-44583" class="comment">
<div id="post-44583-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This answer has helped me a lot! I am struggling a bit though for the code to be able to find the first node as well as the last node in the way as a dead end. With the code you gave it only selects the first node of the way and throws a warning for it. I tried to look into it, it seems as if it already should flag both. The index=-1 refers to the last node according to my understanding. Why would it not throw a warning for the last node in the way that is not connected to two ways?</p>
</div>
<div id="comment-44583-info" class="comment-info">
<span class="comment-age">(01 Aug '15, 20:58)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="44588"></span>
<div id="comment-44588" class="comment">
<div id="post-44588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It works as I expect, if the first node is not connected it warns there, if the last node is not connected it warns there. Maybe you have a typo? I'm not sure where white space is significant and not.</p>
<p>I should mention, the development version of JOSM has added a new pseudoselector, :in-downloaded-area, which should cut down on spurious warnings.</p>
</div>
<div id="comment-44588-info" class="comment-info">
<span class="comment-age">(02 Aug '15, 19:31)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="45304"></span>
<div id="comment-45304" class="comment">
<div id="post-45304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am still struggling to find both the start of a way and the end of a way as a dead end...</p>
<p>Another big question I hope you can help me with: <del>How can I overlay a grid in JOSM and then run the validator individually on each grid square of the total grid. For example, by doing this it will show me the amount of errors for each square of the grid. The grid should be 1,5km^2 and should cover the area of a specified city. How can that be achieved?</del></p>
</div>
<div id="comment-45304-info" class="comment-info">
<span class="comment-age">(16 Sep '15, 21:31)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="45306"></span>
<div id="comment-45306" class="comment">
<div id="post-45306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... is that this question <a href="/questions/45305/how-to-overlay-a-grid-in-josm-and-use-the-validator-on-each-individual-square-of-the-grid">https://help.openstreetmap.org/questions/45305/how-to-overlay-a-grid-in-josm-and-use-the-validator-on-each-individual-square-of-the-grid</a> ?</p>
</div>
<div id="comment-45306-info" class="comment-info">
<span class="comment-age">(16 Sep '15, 21:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="45308"></span>
<div id="comment-45308" class="comment">
<div id="post-45308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well yes, I thought maxerickson could help so asked the question here as well as a separate question so I know maxerickson would read it.</p>
<p>Aseere: If you could help it would be really appreciated.</p>
</div>
<div id="comment-45308-info" class="comment-info">
<span class="comment-age">(16 Sep '15, 22:00)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="45315"></span>
<div id="comment-45315" class="comment not_top_scorer">
<div id="post-45315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BmanS: please place questions only at one place (that prevents double efforts) and preferably at in a new "question" entry (that helps others with the same question). Note: this new question is now answered at the linked place.</p>
</div>
<div id="comment-45315-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 05:47)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44211" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44211-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44150"></span>

<div id="answer-container-44150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44150-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a test in the JOSM validator options labelled "Untagged, empty and one node ways" which is perhaps what you are after.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '15, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '15, 11:51</strong> </span></p>
</div>
</div>
<div id="comments-container-44150" class="comments-container">
<span id="44171"></span>
<div id="comment-44171" class="comment">
<div id="post-44171-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That option seems as if it might help, but it doesn't seem to identify the dead ended roads as errors/warnings? Should it not?</p>
</div>
<div id="comment-44171-info" class="comment-info">
<span class="comment-age">(14 Jul '15, 08:54)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="44172"></span>
<div id="comment-44172" class="comment">
<div id="post-44172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why should a dead end be an error?</p>
</div>
<div id="comment-44172-info" class="comment-info">
<span class="comment-age">(14 Jul '15, 09:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44173"></span>
<div id="comment-44173" class="comment">
<div id="post-44173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it shouldn't be necessarily. But I'm trying to identify dead end roads to check whether they are in fact dead ends or if they are wrongly mapped.</p>
</div>
<div id="comment-44173-info" class="comment-info">
<span class="comment-age">(14 Jul '15, 10:29)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
</div>
<div id="comment-tools-44150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44150-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44151"></span>

<div id="answer-container-44151" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44151-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This validator is a JOSM built-in and always available. You can open it by pressing the blue checkmark icon: <img src="https://wiki.openstreetmap.org/w/images/4/4e/Validation.png" alt="JOSM validator checkmark icon" /></p>
<p>But <em>incomplete ways</em> is probably not what you are looking for. It just "checks for ways with zero or only one node". It won't tell you information like "there is street xyz but it is not mapped in OSM yet".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '15, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '15, 12:23</strong> </span></p>
</div>
</div>
<div id="comments-container-44151" class="comments-container">
&#10;</div>
<div id="comment-tools-44151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44151-form-container" class="comment-form-container">
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

