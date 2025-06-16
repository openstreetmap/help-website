+++
type = "question"
title = "Where can I learn about how Nominatim works? Specifically the algorithm for listing &quot;parent of&quot; objects for a place=* node?"
description = '''Here&#x27;s the background on why I&#x27;m asking. http://forum.openstreetmap.org/viewtopic.php?id=11945 I assume I went to the right place with the detailed problem description and the laundry list of questions. Please feel free to give a short answer here and a more detailed one in the forums (which can oth...'''
date = "2011-04-13T01:45:00Z"
lastmod = "2014-05-30T22:32:00Z"
weight = 4438
keywords = [ "nominatim" ]
aliases = [ "/questions/4438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where can I learn about how Nominatim works? Specifically the algorithm for listing "parent of" objects for a place=\* node?](/questions/4438/where-can-i-learn-about-how-nominatim-works-specifically-the-algorithm-for-listing-parent-of-objects-for-a-place-node)

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
<span id="post-4438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4438-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here's the background on why I'm asking.</p>
<p><a href="http://forum.openstreetmap.org/viewtopic.php?id=11945">http://forum.openstreetmap.org/viewtopic.php?id=11945</a></p>
<p>I assume I went to the right place with the detailed problem description and the laundry list of questions. Please feel free to give a short answer here and a more detailed one in the forums (which can otherwise be frustratingly slow to yield answers).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '11, 01:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '11, 03:16</strong> </span></p>
</div>
</div>
<div id="comments-container-4438" class="comments-container">
<span id="4441"></span>
<div id="comment-4441" class="comment">
<div id="post-4441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How about reading the source?</p>
</div>
<div id="comment-4441-info" class="comment-info">
<span class="comment-age">(13 Apr '11, 07:31)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="4442"></span>
<div id="comment-4442" class="comment">
<div id="post-4442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just like that, huh?</p>
</div>
<div id="comment-4442-info" class="comment-info">
<span class="comment-age">(13 Apr '11, 07:40)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4443"></span>
<div id="comment-4443" class="comment">
<div id="post-4443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The code behind details.php retrieves all objects from a table where parent id is equal to the current id. This does not explain to me who and how assigns parent id to each record, or why it works for parent polygons and does not work for parent nodes. I assume it's not a native OSM relation and is something that a Nominatim data loader, if there is such an animal, must be figuring out as it goes. If I need to look elsewhere, let me know.</p>
</div>
<div id="comment-4443-info" class="comment-info">
<span class="comment-age">(13 Apr '11, 07:53)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4503"></span>
<div id="comment-4503" class="comment">
<div id="post-4503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bump. Is there no documentation, wiki, mailing threads, forum section, etc. on Nominatim data schema? I know the code is fairly well documented, but is that really the only way to learn it? If so, please point me to the source that loads the OSM data into Nominatim and build parent/child relations. I could not find it on the first pass.</p>
</div>
<div id="comment-4503-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 20:55)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4438-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="4449"></span>

<div id="answer-container-4449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4449-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The US county borders and county nodes were created directly from whatever source was available at the time - county node placement is also whatever was used at the time. As you have discovered, Nominatim makes use of these because that's all that is available, but the result are not correct.</p>
<p>The correct solution is to convert the county boundary to a relation:</p>
<ul>
<li>type=boundary</li>
<li>border_type=county</li>
<li>admin_level=6</li>
<li><p>optionally, copy nist:fips_code , nist:state_fips from county boundaries.</p></li>
<li><p>Add county border ways, with role= outer.</p></li>
<li>If the governmental center location is known, add a node with role = admin_centre</li>
<li>Remove the county node.</li>
</ul>
<p>While you're in there working, you can also combine overlapping county ways into a single way and merge any duplicate nodes. If you are working on a state or US border and know where the true boundary lies, you can combine them also.<br />
</p>
<p>For example: <a href="https://www.openstreetmap.org/browse/relation/1357318">https://www.openstreetmap.org/browse/relation/1357318</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '11, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span> </br></p>
</div>
</div>
<div id="comments-container-4449" class="comments-container">
<span id="4455"></span>
<div id="comment-4455" class="comment">
<div id="post-4455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this is good advice for resolving the specific issue I bumped into. I know I included the link to the forum discussion, and your reply there is very much appreciated. But here I am asking about the Nominatim basics. I want to know how node's children are determined. Or, rather, as my question states, <em>where</em> I can learn how node's children are determined and other stuff. There's got to be more documentation on Nominatim, and if not, discussion, than what made it into the wiki.</p>
</div>
<div id="comment-4455-info" class="comment-info">
<span class="comment-age">(13 Apr '11, 19:15)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="21488"></span>
<div id="comment-21488" class="comment">
<div id="post-21488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Mike, I also would like to understand how the internals of Nominatim are working. Preferably without browsing through the code. Did you succeed with your quest for a detailed Nominatim documentation? I have only found this <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">high level overview page</a>. But there are no details. e.g., how is the data base schema organized...</p>
<p>I'll appreciate any direction you can point me at!</p>
</div>
<div id="comment-21488-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 18:23)</span> <span class="comment-user userinfo">konstantin</span>
</div>
</div>
<span id="33570"></span>
<div id="comment-33570" class="comment">
<div id="post-33570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know from Nominatim experimentation:</p>
<ol>
<li><p>admin_level in an administrative border relation is how it determines the parents and children. Lowest number is parent.</p></li>
<li><p>It doesn't matter what border_type is set to on a relation wrt Nominatim. It has assumed named <strong>Ranks</strong>, like 'County' for admin_level 6 in the US. If I create a new relation with border_type set to 'parish', result returned STILL is: County Boundary <em>Test Parish</em>.</p></li>
</ol>
<p>I might suggest we use border_type as 'whatever the administrative boundary's type "name" is'. E.g., Louisiana has parishes, not counties, so border_type=parish ?</p>
</div>
<div id="comment-33570-info" class="comment-info">
<span class="comment-age">(30 May '14, 22:32)</span> <span class="comment-user userinfo">Skybunny</span>
</div>
</div>
</div>
<div id="comment-tools-4449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4449-form-container" class="comment-form-container">
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

