+++
type = "question"
title = "How to tag monasteries?"
description = '''Hello, There are many monasteries around and I was wondering what is the most suitable way to tag them. A monastery (or cloister) is a combination of different things:   church - amenity=place_of_worship; religion=christian; denomination=catholic|orthodox; name=something; building=yes  chapels - ame...'''
date = "2011-03-17T11:15:00Z"
lastmod = "2012-01-20T10:38:00Z"
weight = 3871
keywords = [ "monastery", "tagging", "religion" ]
aliases = [ "/questions/3871" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag monasteries?](/questions/3871/how-to-tag-monasteries)

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
<span id="post-3871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3871-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-3871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>There are many monasteries around and I was wondering what is the most suitable way to tag them.</p>
<p>A monastery (or cloister) is a combination of different things:<br />
</p>
<ul>
<li>church - amenity=place_of_worship; religion=christian; denomination=catholic|orthodox; name=something; building=yes</li>
<li>chapels - amenity=chapel; building=yes</li>
<li>drinking fountains - amenity=drinking_water</li>
<li>fountains used for recreation - ?</li>
<li>gardens (lawns) - landuse=grass(?)</li>
<li>shops selling souvenirs and religious items - shop= ?</li>
<li>monk dormitory - building=yes; building=dorm; another tag?</li>
<li>some monasteries also offer rooms for outsiders, these should be tagged with tourism=hotel|hostel|chalet ?</li>
<li>agricultural buildings - building=yes</li>
</ul>
<p>The monastery is a congregation of all of these. How would you tag it? Area with amenity=monastery surrounding all of it? I haven't seen such a tag in the wiki... Maybe add tag fenced=yes if necessary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-monastery" rel="tag" title="see questions tagged &#39;monastery&#39;">monastery</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-religion" rel="tag" title="see questions tagged &#39;religion&#39;">religion</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '11, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span> </br></p>
</div>
</div>
<div id="comments-container-3871" class="comments-container">
&#10;</div>
<div id="comment-tools-3871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3871-form-container" class="comment-form-container">
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

<span id="3873"></span>

<div id="answer-container-3873" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3873-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-3873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can either make a site-relation adding all the features you mention as belonging to the monastery to it, or draw a polygon around the whole area (the latter gets better evaluated at the moment). All the single features you identified would be usually tagged as suggested by you. For recreational fountains there is <code>amenity=fountain</code>. Agricultural buildings could also be tagged with <code>building=stable/barn</code> instead of <code>yes</code> (I prefer being more specific with buildings, if information is available). The gardens can be tagged as <code>leisure=garden</code> (there is also subtypes for more specific tagging, see the <a href="http://wiki.openstreetmap.org/wiki/Tag:garden:type%3Dmonastery">wiki</a>). Chapels are IMHO also <code>amenity=place_of_worship</code> (<code>building=chapel</code>).</p>
<p>The relation / polygon for the whole monastery would be tagged as <code>amenity=monastery</code> according to <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/monastery">this proposal</a> which also suggests more subtags for further detail. Former monasteries which are not necessarily monasteries as of today are suggested to be tagged with <a href="http://wiki.openstreetmap.org/wiki/Tag:historic%3Dmonastery">historic=monastery</a>. Another alternative is described on the discussion page of place_of_worship: <code>place_of_worship:type</code> but it is far older then the above linked monastery proposal and has never been really used by many mappers, so I'd consider it not active and deprecated by the above mentioned proposals which are in wider use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '11, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '12, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-3873" class="comments-container">
<span id="10094"></span>
<div id="comment-10094" class="comment">
<div id="post-10094-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>adding a "historic=yes" seems useful, too, if the monastery complex is of historic significance. Also a "tourism=attraction" can be used, if the monastery has significant touristic value - think about the Meteora Monasteries in Greece, for example, where tourists are coming in thousands.</p>
</div>
<div id="comment-10094-info" class="comment-info">
<span class="comment-age">(20 Jan '12, 09:58)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="10099"></span>
<div id="comment-10099" class="comment">
<div id="post-10099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd add both in this case, "historic=monastery" and "amenity=monastery" If you have the information, a "start_date=<em>" would enhance detail. And of course "wikipedia=</em>"</p>
</div>
<div id="comment-10099-info" class="comment-info">
<span class="comment-age">(20 Jan '12, 10:38)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-3873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3873-form-container" class="comment-form-container">
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

