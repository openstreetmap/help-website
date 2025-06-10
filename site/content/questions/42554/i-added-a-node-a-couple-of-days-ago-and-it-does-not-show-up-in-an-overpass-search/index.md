+++
type = "question"
title = "I added a node a couple of days ago and it does not show up in an Overpass search"
description = '''(split off from why-havent-my-changes-appeared-on-the-map) There is definitely more to this than the rendering. I added a node a couple of days ago and it does not show up in an Overpass search, either by postcode or by another tag that is present (payment:bitcoin=yes). Other, older nodes with the s...'''
date = "2015-04-23T04:41:00Z"
lastmod = "2015-04-24T05:33:00Z"
weight = 42554
keywords = [ "not_shown", "overpass", "update" ]
aliases = [ "/questions/42554" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I added a node a couple of days ago and it does not show up in an Overpass search](/questions/42554/i-added-a-node-a-couple-of-days-ago-and-it-does-not-show-up-in-an-overpass-search)

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
<span id="post-42554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42554-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><span class="small">(split off from <a href="/questions/4705/">why-havent-my-changes-appeared-on-the-map</a>)</span></p>
<p>There is definitely more to this than the rendering. I added a node a couple of days ago and it does not show up in an Overpass search, either by postcode or by another tag that is present (payment:bitcoin=yes). Other, older nodes with the same tags are showing up no problem, just not the one I added. If I go back into edit mode (on several computers), the node is still there and the tags check out.</p>
<p>Not complaining and there is by no means any kind of rush on this, just a data point and wondering when I will be likely to see it turn up.</p>
<p><em>Update:</em></p>
<p>Wouldn't fit in comment:</p>
<p>OK. I tried it with an ID from the list I retrieved of existing nodes and with the ID as obtained by nevw. Here is what I see:</p>
<p>Guys, this site is breaking on the xml tags. I had to run it through an escaper. The formatting is not very nice now but I hope readable.</p>
<hr />
<p>~/osm$ curl <a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=node(%223463722799%22)%3Bout%3B">http://overpass.osm.rambler.ru/cgi/interpreter?data=node("3463722799")%3Bout%3B</a> &lt;?xml version="1.0" encoding="UTF-8"?&gt;</p>
<p>&lt;osm version="0.6" generator="Overpass API"&gt;</p>
<p>&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;</p>
<p>&lt;meta osm_base="2015-04-19T13:13:02Z"/&gt;</p>
<p>&lt;node id="3463722799" lat="41.0380108" lon="-73.7020693"&gt;</p>
<p>&lt;tag k="addr:city" v="Purchase"/&gt;</p>
<p>&lt;tag k="addr:housenumber" v="630"/&gt;</p>
<p>&lt;tag k="addr:postcode" v="10577"/&gt;</p>
<p>&lt;tag k="addr:state" v="ny"/&gt;</p>
<p>&lt;tag k="addr:street" v="Anderson Hill Road"/&gt;</p>
<p>&lt;tag k="name" v="Purchase Country Market"/&gt;</p>
<p>&lt;tag k="note" v="We accept bitcoin!"/&gt;</p>
<p>&lt;tag k="opening_hours" v="5 - 8 Mon - Sat // 8 - 8 Sundays"/&gt;</p>
<p>&lt;tag k="payment:bitcoin" v="yes"/&gt;</p>
<p>&lt;tag k="phone" v="+1 914 481 4422"/&gt;</p>
<p>&lt;tag k="shop" v="deli"/&gt;</p>
<p>&lt;tag k="website" v="<a href="http://www.purchasecountrymarket.com">http://www.purchasecountrymarket.com</a>"/&gt;</p>
<p>&lt;/node&gt;</p>
<p>&lt;/osm&gt;</p>
<hr />
<p>~/osm$ curl <a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=node(%223469985161%22)%3Bout%3B">http://overpass.osm.rambler.ru/cgi/interpreter?data=node("3469985161")%3Bout%3B</a></p>
<p>&lt;?xml version="1.0" encoding="UTF-8"?&gt;</p>
<p>&lt;osm version="0.6" generator="Overpass API"&gt;</p>
<p>&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;</p>
<p>&lt;meta osm_base="2015-04-19T13:13:02Z"/&gt;</p>
<p>&lt;/osm&gt;</p>
<hr />
<p>Note that I'm having a lot of trouble with logging in to these forums but I'll take that elsewhere. I'm using the temporary token for now.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '15, 04:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e414d90b60f19d3eb918190f1b6f13dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richhhhhh&#39;s gravatar image" />
<p><span>Richhhhhh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richhhhhh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '15, 01:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42554" class="comments-container">
<span id="42555"></span>
<div id="comment-42555" class="comment">
<div id="post-42555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At <a href="http://www.openstreetmap.org">http://www.openstreetmap.org</a> zoom to the location, select the layers tab on the right side, then check 'Map Data', select the node, and then paste the url that you see in the address bar of the browser into your query above by editing it. We will be see too and maybe able to explain any irregularities.</p>
</div>
<div id="comment-42555-info" class="comment-info">
<span class="comment-age">(23 Apr '15, 06:42)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="42556"></span>
<div id="comment-42556" class="comment">
<div id="post-42556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The database of the Overpass API instance must have been synched to the main OSM database. Depending on which instance you are querying this may not have happened. However, as nevw said, please mention a link to such a node (or a location of one).</p>
</div>
<div id="comment-42556-info" class="comment-info">
<span class="comment-age">(23 Apr '15, 08:03)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42562"></span>
<div id="comment-42562" class="comment">
<div id="post-42562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>okay, thanks for the <span>example node</span>. but … what is your problem with it? <a href="http://overpass-turbo.eu/s/8Y7">A Overpass search</a>. Ahh, now I saw that you have posted two queries... I will format this a bit better... Okay, <span>your second example node</span>.</p>
</div>
<div id="comment-42562-info" class="comment-info">
<span class="comment-age">(24 Apr '15, 01:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42563"></span>
<div id="comment-42563" class="comment">
<div id="post-42563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: regarding the markdown problems: see <span>markdown/syntax</span> and use <span>dingus</span> for preview (the live preview here is not showing the real result). XML should work, but it really may not due to whatever problems. Another option: use a pastebin service (if possible a permanent one).</p>
</div>
<div id="comment-42563-info" class="comment-info">
<span class="comment-age">(24 Apr '15, 01:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42554-form-container" class="comment-form-container">
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

<span id="42566"></span>

<div id="answer-container-42566" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42566-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-42566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li><span>example first node</span> is older. The data you see in your paste is from 2015-04-18. The big note text from 2015-04-19 20:44:41 is not yet visible via this Overpass instance.</li>
<li><span>your second example node</span> is existing since 2015-04-21.</li>
</ul>
<p>the <a href="http://overpass.osm.rambler.ru">http://overpass.osm.rambler.ru</a> response says <code>osm_base="2015-04-19T13:13:02Z"</code>.</p>
<p>Apparently, as said in my comment before, the service you are using just has not yet updated its database. "down for mainainance" is <span>currently listed</span> for this service at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction</a></p>
<p>So, try that other Overpass service instance <a href="http://overpass-api.de/api/interpreter?data=node(3469985161)%3Bout%3B">http://overpass-api.de/api/interpreter?data=node(3469985161)%3Bout%3B</a> (second example node) – I get a expected, apparently up to date response there</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '15, 02:00</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '15, 02:07</strong> </span></p>
</div>
</div>
<div id="comments-container-42566" class="comments-container">
<span id="42567"></span>
<div id="comment-42567" class="comment">
<div id="post-42567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. That certainly answers my issue. The node has also appeared on coinmaps.org so it appears that they were probably using the good server but probably a bit slow in updating their own results. I appreciate the time you spent on this.</p>
<p>I've actually ended up using JSON anyway. It was the preview that was giving me issues.</p>
</div>
<div id="comment-42567-info" class="comment-info">
<span class="comment-age">(24 Apr '15, 05:33)</span> <span class="comment-user userinfo">Richhhhhh</span>
</div>
</div>
</div>
<div id="comment-tools-42566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42566-form-container" class="comment-form-container">
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

