+++
type = "question"
title = "Is there a way for me to push my node changes/additions back to OSM?"
description = '''I&#x27;ve been working with streets in cities by collecting ways and their nodes from OpenStreetMap. Sometimes the nodes for a street are good, like this example. Sometimes the street could have a better collection of nodes, like this example which could use a couple more nodes in the middle ... or this ...'''
date = "2014-05-03T22:49:00Z"
lastmod = "2014-05-03T23:45:00Z"
weight = 32849
keywords = [ "ways", "nodes" ]
aliases = [ "/questions/32849" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way for me to push my node changes/additions back to OSM?](/questions/32849/is-there-a-way-for-me-to-push-my-node-changesadditions-back-to-osm)

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
<span id="post-32849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32849-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been working with streets in cities by collecting ways and their nodes from OpenStreetMap. Sometimes the nodes for a street are good, like <a href="http://citystrides.dev/streets/1">this example</a>. Sometimes the street could have a better collection of nodes, like <a href="http://citystrides.dev/streets/181">this example</a> which could use a couple more nodes in the middle ... or <a href="http://citystrides.dev/streets/466">this example</a> which could use a whole lot of nodes added to it.</p>
<p>Ideally, I'd like to work with the nodes in my own site &amp; push my changes back to OpenStreetMap. Is that possible? Then, if it's possible, is it recommended? I know that 'import' type changes are not very welcome (or at least approached with extreme caution), and I'm not sure if these types of changes would fall under that category.</p>
<p>The simplest form of this contribution could be a situation where I add more nodes to a street, and then push those nodes back to OpenStreetMap. I'm looking to find out if there's a more automated way of accomplishing this beyond adding the nodes to my site, and then also manually adding the nodes into OpenStreetMap via iD.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '14, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-32849" class="comments-container">
&#10;</div>
<div id="comment-tools-32849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32849-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="32850"></span>

<div id="answer-container-32850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32850-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-32850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming for a moment that you never make changes to your site that are unsuitable for OSM - then could you not simply build it so that your site retrieves near-immediate updates from OpenStreetMap, and then <em>only</em> make the improvements on OSM (rather than making improvements on your site and then building complex ways to share them back)?</p>
<p>OSM does have an editing API which allows you to upload new or modified versions of objects (in your case, each way improvement would probably mean a few nodes changed, a few created, and a way changed) so you could theoretically build something that contributes your changes back to OSM. Libraries for accessing the OSM API exist for a few programming languages (see <a href="http://wiki.openstreetmap.org/wiki/Frameworks#Single_Purpose_Client_Libraries_for_API0.6_.28the_RESTful_API.29">the wiki</a>) but actually coding stuff yourself is not terribly difficult. However, the more time elapses between loading an OSM object into your system and then uploading an improved version, the greater the danger of a "version conflict" which occurs if someone else has modified the object in the mean time; and resolving these conflicts - keeping their improvement while also uploading yours - is difficult to do in an automated fashion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '14, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 May '14, 23:47</strong> </span></p>
</div>
</div>
<div id="comments-container-32850" class="comments-container">
<span id="32852"></span>
<div id="comment-32852" class="comment">
<div id="post-32852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a good point, about the time between getting info into my site &amp; back out again. Right now, I do very large infrequent imports into my site: one-offs, where I get an entire country's worth of cities (and their streets). So that time would be very large.</p>
</div>
<div id="comment-32852-info" class="comment-info">
<span class="comment-age">(03 May '14, 23:45)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
</div>
<div id="comment-tools-32850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32851"></span>

<div id="answer-container-32851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32851-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-32851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think this wouldn't be possible "in principle", in the end all offline editors do something similar.</p>
<p>However you would need to have reasonably current data on your side or you likely would have endless conflicts, and further you need to implement all the logic that is necessary to correctly modify and add OSM data, for example relation handling, direction dependent tags and so on and so on.</p>
<p>Not a difficult task, just one that takes a significant amount of time and effort.</p>
<p>If you do try to implement your idea, please test against either a private instance of the rails port or one of the dev instances that we offer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '14, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-32851" class="comments-container">
&#10;</div>
<div id="comment-tools-32851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32851-form-container" class="comment-form-container">
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

