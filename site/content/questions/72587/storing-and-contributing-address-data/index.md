+++
type = "question"
title = "Storing and Contributing address data"
description = '''Background: We are building a SaaS that will require a (paying) user to enter an address for works that need to be done. This address (and corresponding lat/lng) will be stored in our database for later displaying on a map if required and the address will be included in emails, pdf&#x27;s as well as bein...'''
date = "2020-01-21T03:32:00Z"
lastmod = "2020-02-09T03:41:00Z"
weight = 72587
keywords = [ "contribute", "commercial", "license" ]
aliases = [ "/questions/72587" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Storing and Contributing address data](/questions/72587/storing-and-contributing-address-data)

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
<span id="post-72587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Background:</strong> We are building a SaaS that will require a (paying) user to enter an address for works that need to be done. This address (and corresponding lat/lng) will be stored in our database for later displaying on a map if required and the address will be included in emails, pdf's as well as being displayed in the software.</p>
<p>We will be using an auto-complete service to make address entry easier and more accurate. We are avoiding google because although there address data is very accurate, there license is very restrictive (and contradictory to their own examples) the license agreement does not allow storing the retrieved address (except for caching) this would require that every time we list 10 addresses on screen, we have to hit the api 10 times and prevents any kind of offline use.</p>
<p><strong>Now to my question:</strong> As the address level data is not very good (particularly in the area's of interest for our initial intended client base) I had the thought of displaying a screen as follows when entering an address: <img src="https://i.ibb.co/yRPyw53/example-Address-Entry.png" alt="alt text" /></p>
<p>This would then store the address (as seen in the 4 fields below the map) and the lat/lng of the address in our database for later use.</p>
<p>Am I able to contribute this data in any way (either live as it happens via an api or once every X weeks/months as a dump) in order to help improve the data?</p>
<p>I have read on another question that I may have to create/get the user to create an account on osm and be able to view their submissions. is there any way we can put in out TOS (or on that screen) that their contributions are given freely and without contributor rights and just give this data completely free of any contribution rights to OSM so it is wholly owned by OSM?</p>
<p>We are really not interested in any kind of recognition or rights of the data as we would still be collecting it anyway and may as well contribute back and improve the data for future use.</p>
<p>If we can, Is there a better way to store this data (say '123', 'Example', 'Avenue') or is just saving '123 Example Avenue' 'city/suburb', 'state', 'country' enough.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-contribute" rel="tag" title="see questions tagged &#39;contribute&#39;">contribute</span> <span class="post-tag tag-link-commercial" rel="tag" title="see questions tagged &#39;commercial&#39;">commercial</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '20, 03:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1e3d654271a067c086e07879db39f59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike16889&#39;s gravatar image" />
<p><span>mike16889</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike16889 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-72587" class="comments-container">
&#10;</div>
<div id="comment-tools-72587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72587-form-container" class="comment-form-container">
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

<span id="72703"></span>

<div id="answer-container-72703" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72703-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mike16889 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can check how others did kind of the same thing :</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/OSMyBiz">OSMyBiz</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Onosm.org">Onosm.org</a></li>
</ul>
<p>Mostly by putting Notes for other mappers to integrate it seems.</p>
<p>I'm not exactly sure of the legal side, but on a practical level, I think you will need to double-check the data and then upload it yourself (or with a company account).</p>
<p>You should be familiar with <a href="https://wiki.openstreetmap.org/wiki/Addresses">address</a> schema and be careful of duplicates.</p>
<p>Once you have a lot of data to contribute, you'll need to check the <a href="https://wiki.openstreetmap.org/wiki/Import">import procedures</a>.</p>
<p>Sorry it's not easier but it's quite impossible for your users to learn how to contribute to OSM in seconds. First example of pitfall that come to my mind is <a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation">address interpolation</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '20, 02:14</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-72703" class="comments-container">
<span id="72915"></span>
<div id="comment-72915" class="comment">
<div id="post-72915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer, gives me a start on where to look.</p>
<p>The state I live in actually provides shape files with property boundaries (polygons) and address (points) under the "Creative Commons Attribution 3.0 Australia Licence" But I do not know enough about these licenses and don't know if it could be incorporated with OSM. If it can be used I am happy to put in the hours of learning the import process and converting the data to a usable format.</p>
</div>
<div id="comment-72915-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 09:40)</span> <span class="comment-user userinfo">mike16889</span>
</div>
</div>
<span id="72917"></span>
<div id="comment-72917" class="comment">
<div id="post-72917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The usual problem with this kind of licenses is that we can't provide the "attribution" part. Once in the OSM database, the source tags can be deleted.</p>
<p>The solution is to ask for a specific waiver to the relevant authorities, I found these <a href="https://wiki.osmfoundation.org/wiki/Licence/Waiver_and_Permission_Templates">templates</a>.</p>
<p>You can then store it on the wiki for future reference.</p>
<p>Actually I found a <a href="https://wiki.openstreetmap.org/wiki/Attribution/sa.data.gov.au_explicit_permission">SA waiver</a> and you can find a <a href="https://wiki.openstreetmap.org/wiki/Contributors#data.gov.au">long list</a> for the rest of Australia.</p>
<p>I hope you can find or add your state !</p>
</div>
<div id="comment-72917-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 10:10)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="72928"></span>
<div id="comment-72928" class="comment">
<div id="post-72928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And for guidelines on the import process, have a look there : <a href="https://wiki.openstreetmap.org/wiki/Category:Data.australia.gov.au_projects">https://wiki.openstreetmap.org/wiki/Category:Data.australia.gov.au_projects</a> .</p>
<p>There is already a lot of work done, with similar datasets.</p>
</div>
<div id="comment-72928-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 17:51)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="72931"></span>
<div id="comment-72931" class="comment">
<div id="post-72931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My state does not appear on the list, I will get onto sending a request as soon as I can. I will probably have to order more ram if the request is accepted, last time I tried to open the full shape file I ran out haha.</p>
</div>
<div id="comment-72931-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 20:08)</span> <span class="comment-user userinfo">mike16889</span>
</div>
</div>
<span id="72948"></span>
<div id="comment-72948" class="comment">
<div id="post-72948-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, good luck on your project ! :-)</p>
<p>As said on the <a href="https://wiki.openstreetmap.org/wiki/Australian_Data_Imports">Australian Data Imports</a> page, you should probably start by a discussion on <a href="https://lists.openstreetmap.org/listinfo/talk-au">talk-au</a>.</p>
<p>For the ram trouble, you'll need to somehow chunk the data anyway.</p>
</div>
<div id="comment-72948-info" class="comment-info">
<span class="comment-age">(08 Feb '20, 15:22)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="72954"></span>
<div id="comment-72954" class="comment not_top_scorer">
<div id="post-72954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Will do, as for the ram i'm just using it as an excuse to get my boss to buy more... For the work I do 16gb is really not cutting it anymore.</p>
</div>
<div id="comment-72954-info" class="comment-info">
<span class="comment-age">(09 Feb '20, 03:41)</span> <span class="comment-user userinfo">mike16889</span>
</div>
</div>
</div>
<div id="comment-tools-72703" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-72703-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72929"></span>

<div id="answer-container-72929" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't see a reason why you can't use the GNAF address data which covers all of Australia, while it isn't available on open license terms, they probably will still work for your application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '20, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72929" class="comments-container">
<span id="72932"></span>
<div id="comment-72932" class="comment">
<div id="post-72932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While this dataset is interesting and would partially work for our needs, we need geocoding and address auto completion for as much of the world as possible. We would end up having to deploy our own server for geocoding for Aus and also hit other api's at the same time and aggregate the results</p>
</div>
<div id="comment-72932-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 20:13)</span> <span class="comment-user userinfo">mike16889</span>
</div>
</div>
</div>
<div id="comment-tools-72929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72929-form-container" class="comment-form-container">
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

