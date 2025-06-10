+++
type = "question"
title = "Using multiple associatedstreet relations for one street"
description = '''I tend to use associatedstreet relations instead of addr:street tags because I see a few advantages. One of the advantages is when a street is made of many different ways, nearby and often parallel (this is typical of housing estates). In this case, I use a different relation for each section of the...'''
date = "2013-11-26T12:42:00Z"
lastmod = "2013-11-28T07:14:00Z"
weight = 28479
keywords = [ "associatedstreet", "relation", "karlsruhe", "address" ]
aliases = [ "/questions/28479" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Using multiple associatedstreet relations for one street](/questions/28479/using-multiple-associatedstreet-relations-for-one-street)

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
<span id="post-28479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28479-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tend to use associatedstreet relations instead of addr:street tags because I see a few advantages.</p>
<p>One of the advantages is when a street is made of many different ways, nearby and often parallel (this is typical of housing estates). In this case, I use a different relation for each section of the street, which makes it unambiguous for a satnav that needs to route to a particular housenumber and might otherwise pick the wrong street segment. In those cases, I also tend to give each relation a distinct name : "streetname west", "streetname north 1", "streetname north 2" instead of a common "streetname" for all of them.</p>
<p>As an aside, if a relation's name is equal to the street name, and is only useful to help mapper identify the correct relation in a list, then it seems silly to tag it : it would be better for the editor to display the member street's name directly.</p>
<p>I decided to ask this question after <a href="http://www.openstreetmap.org/user/Pieren/diary/20385#comment24591">a discussion with Pieren</a> and realising that <a href="http://osmose.openstreetmap.fr/en/map/">osmose</a> flags multiple relations per street as <a href="http://wiki.openstreetmap.org/wiki/Osmose/erreurs#Tags_missing">error 2060</a>. Obviously, some people frown upon multiple relations per street and/or relation names that do not match the street name.</p>
<p>What do people here think about multiple relations per street and distinct relation names ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-associatedstreet" rel="tag" title="see questions tagged &#39;associatedstreet&#39;">associatedstreet</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-karlsruhe" rel="tag" title="see questions tagged &#39;karlsruhe&#39;">karlsruhe</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '13, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-28479" class="comments-container">
<span id="28500"></span>
<div id="comment-28500" class="comment">
<div id="post-28500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wonder whether the routing aspect will actually get any better with relation(s). Most of the time you don't want to drive to a specific POI but instead to a nearby parking place, unless you travel by foot.</p>
</div>
<div id="comment-28500-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 18:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="28532"></span>
<div id="comment-28532" class="comment">
<div id="post-28532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In many areas you can park right in front of the POI/house, and a nearby car park is not needed.</p>
</div>
<div id="comment-28532-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 09:13)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28479-form-container" class="comment-form-container">
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

<span id="28487"></span>

<div id="answer-container-28487" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28487-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can see a use of a single relation to simplify downloading all sections of a street, but cannot see a benefit of multiple associatedStreet relations. For any style of address tagging - with or without relations, a router will find the closest geometrically matched street segment as a destination.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-28487" class="comments-container">
<span id="28492"></span>
<div id="comment-28492" class="comment">
<div id="post-28492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Routing problems begin when the street which is geometrically closest to the house is not the correct one to drive to.</p>
<p>It's not <em>that</em> frequent but it happens. Often near a corner, a barrier, or a oneway segment, but can be anywhere.</p>
<p>One of the original purpose of AS relations is to replace the geometry heuristic with something less ambiguous. So I guess it boils down to wether using multiple relations fixes some ambiuity.</p>
</div>
<div id="comment-28492-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 14:56)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28487-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28497"></span>

<div id="answer-container-28497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28497-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sad that you ask a question in English based on a discussion in French... and this help site is not the right place to talk about disputed stuff (better on the forum or one mailing list).<br />
Anyway, I will repeat my argument here : the relation "associatedStreet" is supposed to represent the street and its house numbers. The tag "name" should not be used for another purpose like routing instructions etc but just give the street name itself (as an optional hint, as said <a href="http://wiki.openstreetmap.org/wiki/Relation:associatedStreet">on the wiki</a>). Otherwise you create unnecessary confusion if the tag name differs between the relation and the highway, especially for newcomers.<br />
In addition, I could say that OSM is a geodatabase as you know. It's not necessary to write in plain text which segment is 'north' and which one is 'south'. It's all defined in nodes coordinates. We might have to create some additional tags helping navigation systems but certainly not in the street 'name' tag itself.<br />
The point you raise about the editor, that it should display the 'name' tag from the street member is hard to solve and support in long term. Basically, the editors display all relations in the same way. They cannot check each relation members based on all possible relations types to find which one contains the expected 'name' text to display on the info widget.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 16:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '13, 16:56</strong> </span></p>
</div>
</div>
<div id="comments-container-28497" class="comments-container">
<span id="28501"></span>
<div id="comment-28501" class="comment">
<div id="post-28501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, switched to English to reach wider audience. You're right, maybe ML would have been a better medium, it's just not one I'm as comfortable with.</p>
<p>I never said that the relation name had anything to do with routing, not sure how you reached that conclusion.</p>
</div>
<div id="comment-28501-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 18:03)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="28502"></span>
<div id="comment-28502" class="comment">
<div id="post-28502-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You never state your view on the relation's name's purpose (only what its value should be).</p>
<p>If the purpose is just "help editing", then using distinct names when there are multiple relations for one street makes logical sense to me.</p>
<p>If (for whatever reason) the only accepted values are "absent" and "identical to the street's name", then I'd rather leave it out and let the editor figure out the display name automatically. Looking at a relation's members really shouldn't be hard ? Using a fallback if the member hasn't been downloaded is ok.</p>
</div>
<div id="comment-28502-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 18:11)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28497-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28495"></span>

<div id="answer-container-28495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28495-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I like the idea of using associatedStreet to indicate routing, although I wonder if it couldn't better be done by adding in a driveway or similar structure. One assumes there is some kind of an access road or path, tagged correctly to indicate who can use it. Can you give an example of where the geometrically closest segment isn't the correct one?</p>
<p><em>Creating</em> a name for them, however, is, in my opinion, completely wrong. If the street isn't actually called that name, it shouldn't be tagged with that name. At most, you could put a more descriptive name for use by mappers in the <strong>note</strong> tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/25d131767ead24f236c3f9e856f1358c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JDub&#39;s gravatar image" />
<p><span>JDub</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JDub has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-28495" class="comments-container">
<span id="28499"></span>
<div id="comment-28499" class="comment">
<div id="post-28499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://osm.org/go/esz2ImAHt?m=">here</a> is a example where the geometry heuristic would get it wrong and would be fixed by using multiple relations (addresses not surveyed yet, I'm working on it :p).</p>
<p>When I suggest using distinct <em>name</em> tags, it is of course for the relation and not for the actual street. AFAICT, the relation name's sole purpose is to help editing. It isn't processable "map data" per se.</p>
</div>
<div id="comment-28499-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 17:52)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28495-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28503"></span>

<div id="answer-container-28503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28503-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Belgium we use the associatedStreet in the same way as Pieren describes: containing all street segments and houses/address points. We also add postal code and city to the relation tags in the hope that we do not have to repeat them on every single building. (we do not have areas for the post code (yet)).</p>
<p>The idea of the OP is completely different and will make it impossible for tool developers to know how they have to represent/use the relation. I hope that there will be only 1 unambiguous definition for the associatedStreet-relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-28503" class="comments-container">
<span id="28531"></span>
<div id="comment-28531" class="comment">
<div id="post-28531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sounds like the kind of counter-example I was wondering about, but I don't understand how multiple relations would "make it impossible for tool developers to know how they have to represent/use the relation" ? Can you give an example of how it makes things harder for tools ?</p>
</div>
<div id="comment-28531-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 09:10)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="28538"></span>
<div id="comment-28538" class="comment">
<div id="post-28538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because in our case the name of the street is the name of the associatedStreet relation and you "invent" a name. We want the tools to use the name of the associatedStreet relation, not the one on the road. This is needed in cases where a street has a different names on the left and right side of the street. This happens a lot when the street is the border between 2 villages.</p>
</div>
<div id="comment-28538-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 11:03)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="28545"></span>
<div id="comment-28545" class="comment">
<div id="post-28545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How is the relation's name any better than the street's dual names in this case ? AFAIK nominatim uses the street name, not the relation name. Which tool uses the relation name ?</p>
</div>
<div id="comment-28545-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 15:46)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="28567"></span>
<div id="comment-28567" class="comment">
<div id="post-28567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems that no tool uses the name of the relation. However, this is the way we interpreted the associatedStreet relation in Belgium. It would be nice that one does not have to repeat the name on the roads and the buildings, only once on the relation should be sufficient. Otherwise the relation is pretty useless IMHO.</p>
<p>As I wrote, the street has two names, but the houses on either side of the street only have 1 street name. When you could put those houses together with the street segments in a relation and give that relation a name, postcode, city etc; one could form the complete address.</p>
</div>
<div id="comment-28567-info" class="comment-info">
<span class="comment-age">(28 Nov '13, 04:50)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="28571"></span>
<div id="comment-28571" class="comment">
<div id="post-28571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you are not putting the name on the street but instead on the associatedStreet relation? Doesn't this break pretty much any tool out there?</p>
</div>
<div id="comment-28571-info" class="comment-info">
<span class="comment-age">(28 Nov '13, 06:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="28572"></span>
<div id="comment-28572" class="comment not_top_scorer">
<div id="post-28572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We still put the name on the street too, but if OSM was designed from the beginning with associatedStreets, we should not have to do that. Anyway, I described what we currently do with associatedStreets in Belgium, but since there is no support for it (read tools), I doubt whether I will continue to create them. Several people in Belgium will continue to use it the way I described: put name, postcode, city as tags on the relation and hope a tool (e.g. Nominatim) will use those instead of using other rules</p>
</div>
<div id="comment-28572-info" class="comment-info">
<span class="comment-age">(28 Nov '13, 07:14)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-28503" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-28503-form-container" class="comment-form-container">
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

