+++
type = "question"
title = "How often the osm_id was unsolicitedly-changed, what the risk before 2020?"
description = '''This question is not about &quot;natural changes&quot; (e. g. user editions deleting something), is about system-maintenance events that changed (or will change) the value of the osm_id.  Any relation have an unique ID, the so-called osm_id, as in an XML element, &amp;lt;relation id=&quot;123&quot;&amp;gt;. Ways and nodes also...'''
date = "2018-10-31T01:22:00Z"
lastmod = "2018-11-01T17:26:00Z"
weight = 66577
keywords = [ "changes", "osm_id" ]
aliases = [ "/questions/66577" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How often the osm_id was unsolicitedly-changed, what the risk before 2020?](/questions/66577/how-often-the-osm_id-was-unsolicitedly-changed-what-the-risk-before-2020)

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
<span id="post-66577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66577-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This question is <strong>not</strong> about "natural changes" (e. g. user editions deleting something), is about system-maintenance events that changed (or will change) the value of the <code>osm_id</code>.</p>
<hr />
<p>Any relation have an unique ID, the so-called <code>osm_id</code>, as in an XML element, &lt;relation id="123"&gt;. Ways and nodes also have respectives <code>osm_id</code>s. The <code>osm_id</code> is also used in SQL data dumps, etc. URLs use the notation <code>relation/123</code> or <code>way/123</code> or <code>node/123</code>.</p>
<p>As we can check, some <code>osm_id</code> was preserved, the element's <code>osm_id</code> value stay unchanged many years: <a href="https://www.openstreetmap.org/node/1/history">node 1 is there!</a> ... But "all OSM people" say that a maintenance event can change <code>osm_id</code> values, the system can rebuild it. Therea are a "risk of change". The focus here is this kind of "unsolicited changes" of the maintenance/recovery events, and <strong>the risk of an event changing the <code>osm_id</code> value (whitout editions)</strong>.</p>
<p><strong>NOTE</strong>: is natural to change, the reality is dynamic (an earthquake destroys map features) and the community enhance map features editing it (e. g. a node is deleted to become a complete relation)... But the focus here is not the "natural changes".<br />
A crash in the OSM servers or a big technical change can enforce the system to <em>rebuild</em> <code>osm_id</code>'s (some or all). Whe can label this kind of changes as <strong>unsolicited changes</strong>.</p>
<p>For many applications is possible to suppose that, <strong>in the application's "time perspective", the <code>osm_id</code> not changes</strong>. But in a <em>digital preservation</em> perspective, and other more specific applications, the "risk of <code>osm_id</code> change" exists. In a perspective of 10 years, the change will occur... Is it?</p>
<h2 id="where-the-information-about-unsolicited-changes-of-osm_id">Where the information about unsolicited changes of osm_id?</h2>
<p>With some basic information we can ask any question about "unsolicited changes of <code>osm_id</code>".</p>
<p>How many times the <code>osm_id</code> changed for all elements <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">since 2009</a>? A specific group of elements (how many?) suffered a technical maintenance that affected its <code>osm_id</code>?</p>
<p>What the risk that an element created today experiencing unsolicitedly-change of its <code>osm_id</code> before 2020?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '18, 01:22</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '18, 10:04</strong> </span></p>
</div>
</div>
<div id="comments-container-66577" class="comments-container">
<span id="66621"></span>
<div id="comment-66621" class="comment">
<div id="post-66621-score" class="comment-score">
2
</div>
<div class="comment-text">
<blockquote>
<p>But "all OSM people" say that a maintenance event can change osm_id values, the system can rebuild it. Therea are a "risk of change".</p>
</blockquote>
<p>No, "all OSM people" do <em>not</em> mean maintenance events when warning about referencing OSM IDs and talking about permanent IDs. The "risk of change" refers to edits that make an ID reference loose it's original meaning, which depends on the use-case.</p>
<blockquote>
<p>the element's osm_id value stay unchanged many years: node 1 is there!</p>
</blockquote>
<p>Well, the ID itself is still there, but the element node 1 represents has changed many times: tree in Germany (v13), buoy in the Atlantic Ocean (v15), memorial stone in London (v17), bike rental in Edinburgh (v19). Not what data consumers would expect (but still OK in this case because of the deletes in between). This is not a problem if you update a regular osm2pgsql rendering database, but it is e.g. if you link your restaurant rating database to OSM IDs and suddenly you are rating a tree (v13) instead of a restaurant (v11) – and the restaurant you actually meant now has node ID 2614114739.</p>
</div>
<div id="comment-66621-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 17:26)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-66577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66577-form-container" class="comment-form-container">
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

<span id="66587"></span>

<div id="answer-container-66587" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66587-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ppKrauss has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no reason why a technical event (aka server crash etc) would require a renumbering of OSM objects, the ids are one of the objects attributes and not a transient database row id or similar.</p>
<p>Naturally some of the data model changes that are in discussion (area types, doing away with way nodes and similar) could potentially lead to a large number of objects being removed and new ones with different id being created, however any such change would be discussed and prepared well in advance.</p>
<p>So to answer your question, the likelihood of any such change happening before 2020 is minimal.</p>
<p>Note: none of the above makes relying on stable OSM ids less technically defective.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '18, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '18, 10:07</strong> </span></p>
</div>
</div>
<div id="comments-container-66587" class="comments-container">
<span id="66588"></span>
<div id="comment-66588" class="comment">
<div id="post-66588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/2053/simonpoole"></a><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>, good answer. Well, there are "no risk"? The "no risk" is a goos news (!), but not seems a reliable information (is it? some link to authoritative assertion?)... It is a <a href="https://wiki.openstreetmap.org/wiki/Permanent_ID">contradiction with the motivations that lead people to propose a <code>perma_id</code></a>.</p>
</div>
<div id="comment-66588-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:08)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66589"></span>
<div id="comment-66589" class="comment">
<div id="post-66589-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14889/ppkrauss">@ppKrauss</a> - if you're trying to have a general discussion about something, then the help site's question-and-answer format isn't well suited to it. You'd be better off on one of the mailing lists.</p>
</div>
<div id="comment-66589-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66590"></span>
<div id="comment-66590" class="comment">
<div id="post-66590-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Note the help site is not a general discussion facility. Still just one point, the problem with perma ids for POIs and similar objects is, that it is simple to determine that an object is unchanged and can retain the same id, but that it is practically impossible to achieve consensus on what an id changing event should be.</p>
<p>Consider a restaurant and all the different ways certain fundamental attributes of it can change.</p>
</div>
<div id="comment-66590-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="66591"></span>
<div id="comment-66591" class="comment">
<div id="post-66591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole"></a><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>, no need for mailing lists... And sorry my English. If there are a place with the "official information" that <code>osm_id</code> not changes, will be a complete answer. You have my up-vote, it is only a complement to mark as accepted: request for authoritative URL is usual at Stackoverflow.</p>
</div>
<div id="comment-66591-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:21)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66593"></span>
<div id="comment-66593" class="comment">
<div id="post-66593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The nature of the id is essentially implicit through the data model and API definition. In practical terms you should probably refer to the rails-port database definition <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/db/structure.sql">https://github.com/openstreetmap/openstreetmap-website/blob/master/db/structure.sql</a></p>
</div>
<div id="comment-66593-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:28)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="66594"></span>
<div id="comment-66594" class="comment not_top_scorer">
<div id="post-66594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/db/structure.sql">good link</a>, now I have a better "big picture"... Well, sorry to ask again, is only a last check: no event of <code>schema_migrations</code> changed (some) <code>osm_id</code> values? (... and I not see if <code>schema_migrations</code> is only a "rails-port database" schema)</p>
</div>
<div id="comment-66594-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:37)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66595"></span>
<div id="comment-66595" class="comment not_top_scorer">
<div id="post-66595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>All migrations back to 2007 <a href="https://github.com/openstreetmap/openstreetmap-website/commits/master/db/migrate">https://github.com/openstreetmap/openstreetmap-website/commits/master/db/migrate</a> can be found here. Naturally a renumbering could have happened by a different mechanism. In any case since the introduction of API 0.5 (removal of segments) there have been no changes to the data model that have changed ids.</p>
</div>
<div id="comment-66595-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:44)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="66597"></span>
<div id="comment-66597" class="comment not_top_scorer">
<div id="post-66597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot <a href="https://help.openstreetmap.org/users/2053/simonpoole"></a><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> (!). For readers: I selected this answer as "correct" by these additional information posted as comments. PS: the link is saved as evidence at <a href="https://web.archive.org/web/20181031110330/https://github.com/openstreetmap/openstreetmap-website/commits/master/db/migrate">https://web.archive.org/web/20181031110330/https://github.com/openstreetmap/openstreetmap-website/commits/master/db/migrate</a></p>
</div>
<div id="comment-66597-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:55)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-66587" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66587-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66579"></span>

<div id="answer-container-66579" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66579-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you wrote osm_ids refer to nodes, ways and relations. Mappers can at any time change the "definition" of such an object. An example a node that represents a postal_box today, can be moved by any mapper, the tags can be changed and it can represent a shop=toys at the next moment. The same is true for ways and relations. Things that are mapped as a node today, might be mapped as a closed way tomorrow. The original node can become one of the nodes of the closed way, but it lost all it's tags and no longer represent the POI.</p>
<p>Some changes are unlikely, but you can never assume that the osm_id represents the same object between 2 data dumps. To answer your question "how many times the osm_id changed since 2009, well it depends on the object you are looking at. Some might never have changed (i.e. they still represent the original object), others might have changed several times.</p>
<p>There was also a technical change since the beginning of the project, ids were changed from 32 bit to 64 bit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '18, 05:22</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-66579" class="comments-container">
<span id="66580"></span>
<div id="comment-66580" class="comment">
<div id="post-66580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>. Where the information (to audit) about what you expressed as "changed several times", can I count or check time-line? About "it depends on the object you are looking at", I not looking for user-deletions, etc. But <strong>unsolicited</strong> or undesired changes, like something caused by a server crash or techinal changes (imagine something as the change to 64 bit changing all <code>osm_id</code> values).</p>
</div>
<div id="comment-66580-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 08:47)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-66579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66579-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66581"></span>

<div id="answer-container-66581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66581-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have personally deleted relations and re-created them under a new ID when their version counter reached four digits, adding a "note" or similar link to point to the old ID. This is not super elegant but easier to handle for mappers who would otherwise often see a timeout when trying to access object history.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '18, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66581" class="comments-container">
<span id="66583"></span>
<div id="comment-66583" class="comment">
<div id="post-66583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi @FrederikRamm, I edited the question, now I am defining what is <em>unsolicited change</em> of the <code>osm_id</code>... Please explain this problem of "version counter reached four digits", I never see: the system enforced you to delete? Was not a "natural change" to enhance the map feature?</p>
</div>
<div id="comment-66583-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 09:05)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-66581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66581-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66584"></span>

<div id="answer-container-66584" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66584-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends. What sort of object is it? Was it roughly drawn or imported and likely to be refined later? Is it in an area where people are more likely to remap rather than ensure object ID reuse?</p>
<p>Rather than guessing, what I'd suggest that you do is it look at some of the objects of the type that you are interested in in an area that you are interested in and see how much reuse has occurred over the years (since the licence change). That, and only that, will start to answer your question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '18, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-66584" class="comments-container">
<span id="66585"></span>
<div id="comment-66585" class="comment">
<div id="post-66585-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Node 1 has been various things in various places over the years as one example: <a href="https://www.openstreetmap.org/node/1/history">https://www.openstreetmap.org/node/1/history</a></p>
</div>
<div id="comment-66585-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 09:11)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="66586"></span>
<div id="comment-66586" class="comment">
<div id="post-66586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneElse</a> I edited the question's title to avoid confusion, it is about <strong>unsolicited changes</strong> of the <code>osm_id</code> values, as in a technical maintenance event.</p>
</div>
<div id="comment-66586-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 09:18)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66592"></span>
<div id="comment-66592" class="comment">
<div id="post-66592-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Low-ID nodes are especially prone to movement, partly by accident (node 1 was accidentally moved only yesterday, which resulted in the historical "Greenwich Meridian" being somewhat inaccurate in OSM), and partly by design (mappers have been known to replace low-id nodes in features with higher ones to prevent accidental moves)</p>
</div>
<div id="comment-66592-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 10:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66584-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

