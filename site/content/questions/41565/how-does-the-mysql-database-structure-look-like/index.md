+++
type = "question"
title = "How does the mysql database structure look like?"
description = '''Hi! Could someone please post the structure of a mysql-database for OSM? (a pasteable sql would be great from phpmyadmin for example) Greetings John (I&#x27;m happy I found this help.openstreetmap.org page. It seems not to be linked on the main page. And the forum that I found before isn&#x27;t so handy as th...'''
date = "2015-03-08T23:42:00Z"
lastmod = "2015-03-11T07:49:00Z"
weight = 41565
keywords = [ "table", "database", "structure", "sql", "mysql" ]
aliases = [ "/questions/41565" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does the mysql database structure look like?](/questions/41565/how-does-the-mysql-database-structure-look-like)

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
<span id="post-41565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41565-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! Could someone please post the structure of a mysql-database for OSM? (a pasteable sql would be great from phpmyadmin for example)</p>
<p>Greetings John</p>
<p>(I'm happy I found this help.openstreetmap.org page. It seems not to be linked on the main page. And the forum that I found before isn't so handy as this help-systen here.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-structure" rel="tag" title="see questions tagged &#39;structure&#39;">structure</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '15, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/bd22ae7be4920107ca423b9cc035185d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John215&#39;s gravatar image" />
<p><span>John215</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John215 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41565" class="comments-container">
<span id="41566"></span>
<div id="comment-41566" class="comment">
<div id="post-41566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not to answer your question, but for the avoidance of doubt, help.openstreetmap.org is linked to from <a href="http://www.openstreetmap.org/help">http://www.openstreetmap.org/help</a> (from the help button on openstreetmap.org), along with the "welcome" page and the wiki.</p>
</div>
<div id="comment-41566-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 00:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41565-form-container" class="comment-form-container">
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

<span id="41567"></span>

<div id="answer-container-41567" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41567-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John215 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no "the mysql database" - see <a href="http://wiki.openstreetmap.org/wiki/MySQL">this page</a> for info.</p>
<p>If you want to know about the "main" OpenStreetMap PostgreSQL database (used by what is referred to as the "Rails Port") see <a href="http://wiki.openstreetmap.org/wiki/The_Rails_Port">here</a> and <a href="https://github.com/openstreetmap/openstreetmap-website">here</a>, and follow the links from those pages. If you want to know about how to store data so that it can be rendered, then the actual database structure can depend on the data selected to be rendered. <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style">This file</a> determines the columns used by OpenStreetMap's "standard" style.</p>
<p>Of course, depending on what you want to do with OSM data, it's perfectly possible to think of ways to store it in MySQL, so a bit more information about what you're trying to do here would really help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '15, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-41567" class="comments-container">
<span id="41568"></span>
<div id="comment-41568" class="comment">
<div id="post-41568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically I just want all data in a db to be able to do many queries on it, to get preprocessed data. - I already found part of your links. I still asked because there are other pages on the wiki that still explicitly talk about the possibility to use mysql. As I only found this help-system here today, I only was able to find a similiar question today. The user asking had obviously the same error as I had. Your last link seems most helpful. I'll wait a bit before I mark your answer as accepted; maybe someone posts a working example for mysql-import of an osm-file - but I doubt that.</p>
</div>
<div id="comment-41568-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 01:20)</span> <span class="comment-user userinfo">John215</span>
</div>
</div>
<span id="41578"></span>
<div id="comment-41578" class="comment">
<div id="post-41578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm just curious. Is it possible to see those of my comments, that were deleted? (And who they were deleted by?)</p>
</div>
<div id="comment-41578-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 15:10)</span> <span class="comment-user userinfo">John215</span>
</div>
</div>
<span id="41579"></span>
<div id="comment-41579" class="comment">
<div id="post-41579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10629/john215">@John215</a> It wasn't me that deleted them :) I received the notification emails for them but they were gone when I read the question. I'm not aware of a way of seeing revisions of a deleted comment. Maybe have a look over on <a href="http://meta.osqa.net/">http://meta.osqa.net/</a> , but probably not worth asking there as it's pretty moribund these days.</p>
</div>
<div id="comment-41579-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 15:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="41584"></span>
<div id="comment-41584" class="comment not_top_scorer">
<div id="post-41584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ty again for your reply. I really wanted to know, before I hit accept at your answer. What I posted: It was 100% along what should go into the comments. I will add some of it later to my original question. - And then I wrote about stackoverflow: Yes, those were two offtopic sentences. But just look, someone complains at SO I would have made a crosspost there, because of here! SO=OSM? Lol</p>
</div>
<div id="comment-41584-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 17:16)</span> <span class="comment-user userinfo">John215</span>
</div>
</div>
<span id="41585"></span>
<div id="comment-41585" class="comment not_top_scorer">
<div id="post-41585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now I remember what else I wrote and why probably it was deleted. I wrote that the other user got downvoted on his last question on here, and is now inactive.</p>
</div>
<div id="comment-41585-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 17:19)</span> <span class="comment-user userinfo">John215</span>
</div>
</div>
<span id="41617"></span>
<div id="comment-41617" class="comment">
<div id="post-41617-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should either completely avoid making <a href="https://stackoverflow.com/questions/28927803/whats-the-table-structure-for-mysql-to-import-osm-via-osmembrane-and-osmosis">crossposts</a> or mention them in every question. Otherwise you are wasting ressources by letting multiple people think about your problems that have probably already been solved elsewhere. It also makes finding the solution easier for other people having the same problem.</p>
</div>
<div id="comment-41617-info" class="comment-info">
<span class="comment-age">(10 Mar '15, 17:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="41621"></span>
<div id="comment-41621" class="comment not_top_scorer">
<div id="post-41621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai"></a><a href="http://help.openstreetmap.org/users/158/scai">@scai</a>: Just to put it straight, I make one comment to this: I first posted on stackoverflow a couple of questions about OSM, and I never got a real answer there, because most people over there simply don't know. - If you would mind to read the text consciously that you are commenting on, you would know by now, that I only yesterday found this help system here on OSM - and then I immediatly made an account here and asked here. And see! Here I got the right answer. Plain, fast, exactly to the point. (Ty again <a href="http://help.openstreetmap.org/users/387/someoneelse"></a><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>!) - (No Ty to you, Scai, sorry.) And OSM!=SO.</p>
</div>
<div id="comment-41621-info" class="comment-info">
<span class="comment-age">(10 Mar '15, 20:41)</span> <span class="comment-user userinfo">John215</span>
</div>
</div>
<span id="41622"></span>
<div id="comment-41622" class="comment not_top_scorer">
<div id="post-41622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai"></a><a href="http://help.openstreetmap.org/users/158/scai">@Scai</a>: Now that I am at it, a really last comment. I also found similiar questions on stackoverflow, that were some years old, and got no answer, or even got downvoted. - Most people over there just do not know anything about OSM, at least when it comes to putting a 40+GByte osm-file into a database. Answers on that specific topic usually use words like: Should, may, might, could, and 'I haven't tried it myself'.</p>
</div>
<div id="comment-41622-info" class="comment-info">
<span class="comment-age">(10 Mar '15, 20:47)</span> <span class="comment-user userinfo">John215</span>
</div>
</div>
<span id="41629"></span>
<div id="comment-41629" class="comment">
<div id="post-41629-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10629/john215"></a><a href="http://help.openstreetmap.org/users/10629/john215">@John215</a>: Stack Overflow is about <em>programming</em>. Your question is not about programming, hence it is completely offtopic for Stack Overflow and people will start downvoting it. However it might be ontopic for <a href="http://gis.stackexchange.com">http://gis.stackexchange.com</a> where you will also find way more more people with OSM knowledge than at SO. Also you didn't really get my point from my previous comment. And this is the wrong place for this discussion.</p>
</div>
<div id="comment-41629-info" class="comment-info">
<span class="comment-age">(11 Mar '15, 07:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41567" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41567-form-container" class="comment-form-container">
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

