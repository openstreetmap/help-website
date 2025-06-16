+++
type = "question"
title = "highway = crossing and highway_1 = traffic_signals. It&#x27;s right?"
description = '''I need to add the passage of pedestrians and the traffic signal at the same point of the track. I intend to do so: - Highway=crossing - Highway_1=traffic_signals. It&#x27;s correct? Otherwise, what is the correct way? (original text in Portuguese, translated into English with google translator)'''
date = "2015-07-08T16:47:00Z"
lastmod = "2015-07-10T14:03:00Z"
weight = 44045
keywords = [ "traffic_signals" ]
aliases = [ "/questions/44045" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [highway = crossing and highway_1 = traffic_signals. It's right?](/questions/44045/highway-crossing-and-highway_1-traffic_signals-its-right)

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
<span id="post-44045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44045-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to add the passage of pedestrians and the traffic signal at the same point of the track.</p>
<p>I intend to do so: - Highway=crossing - Highway_1=traffic_signals.</p>
<p>It's correct? Otherwise, what is the correct way?</p>
<p>(original text in Portuguese, translated into English with google translator)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '15, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/62b0db5708737186a53757d471a515ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seth&#39;s gravatar image" />
<p><span>seth</span><br />
<span class="score" title="201 reputation points">201</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seth has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44045" class="comments-container">
&#10;</div>
<div id="comment-tools-44045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44045-form-container" class="comment-form-container">
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

<span id="44105"></span>

<div id="answer-container-44105" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44105-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="seth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Start using JOSM :-) No, just kidding.</p>
<p>I do not combine the highway=traffic_signals with the highway=crossing node.</p>
<p>The highway=traffic_signals tag typically goes on the crossing of the 2 roads. I place the highway=crossing node where the road crosses the zebra. On the latter node I also add crossing=traffic_signals.</p>
<p>I have see some variations on this. like highway=traffic_signals ; crossing=traffic_signals on the node where the 2 ways cross. The more recent versions of josm show a large and a small traffic signal icon on such a node.</p>
<p>So the reason that there are so many crossing=zebra is that iD makes a mistake IMHO (and compared to the wiki). This should be reported, not ? But you can always override the value that iD adds for a tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '15, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-44105" class="comments-container">
<span id="44109"></span>
<div id="comment-44109" class="comment">
<div id="post-44109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For e.s.c.a.d.a .: I think this complicated issue. I think he should really be better debated, to define a common standard to everyone, which is difficult. I do not use the JOSM because it is incompatible with Chromebooks.</p>
<p>Here's a link the intersection in question. analyze and see if it's correct: <a href="https://www.openstreetmap.org/edit?node=3641052960#map=20/-20.46169/-54.61949">https://www.openstreetmap.org/edit?node=3641052960#map=20/-20.46169/-54.61949</a></p>
</div>
<div id="comment-44109-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 13:08)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44110"></span>
<div id="comment-44110" class="comment">
<div id="post-44110-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just updated the crossing in the way I would tag it, using iD. So my solution has nothing to do with the editor. See <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals">traffic signals wiki page</a> simple intersections why a single traffic signal node in the middle works</p>
<p>There are now 5 nodes, one for each zebra crossing, 1 for the place where the two roads intersect</p>
</div>
<div id="comment-44110-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 13:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44111"></span>
<div id="comment-44111" class="comment">
<div id="post-44111-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>feel free to change it back to a form to which you are more comfortable with, but I would try to avoid using anything with "_1" at the end.</p>
</div>
<div id="comment-44111-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 13:17)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44114"></span>
<div id="comment-44114" class="comment">
<div id="post-44114-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, now I understand. I will do so: highway = crossing, crossing = traffic_signals, crossing_ref = zebra, which is what actually occurs at the intersection.</p>
<p>The highway = traffic_signals (as escada- suggested) at the intersection of routes as a single signal, do not think that is the most correct because the intersection has two signals.</p>
<p>Thank you for your patience.</p>
</div>
<div id="comment-44114-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 14:03)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
</div>
<div id="comment-tools-44105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44105-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44047"></span>

<div id="answer-container-44047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44047-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-44047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>highway=crossing crossing=traffic_signals</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '15, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-44047" class="comments-container">
<span id="44049"></span>
<div id="comment-44049" class="comment">
<div id="post-44049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As documented on the corresponding <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals#Traffic_signals_for_pedestrians">wiki page</a></p>
</div>
<div id="comment-44049-info" class="comment-info">
<span class="comment-age">(08 Jul '15, 20:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44051"></span>
<div id="comment-44051" class="comment">
<div id="post-44051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thank you.</p>
</div>
<div id="comment-44051-info" class="comment-info">
<span class="comment-age">(08 Jul '15, 23:39)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44082"></span>
<div id="comment-44082" class="comment not_top_scorer">
<div id="post-44082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It does not work because the highway = crossing already included the crossing = zebra. So I can not include a crossing_1 = traffic_signals.</p>
<p>Would otherwise do?</p>
</div>
<div id="comment-44082-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 18:58)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44083"></span>
<div id="comment-44083" class="comment not_top_scorer">
<div id="post-44083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This should be crossing_ref=zebra (&amp; this is a GB specific thing, a Zebra crossing is highway=crossing crossing=uncontrolled crossing_ref=zebra). Personally I've always found the crossing tagging a little obscure. Your question reinforces my feeling that it is not intuitive.</p>
</div>
<div id="comment-44083-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 19:16)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="44086"></span>
<div id="comment-44086" class="comment not_top_scorer">
<div id="post-44086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As SK53 said, highway=crossing,crossing=traffic_signals,crossing_ref=zebra. I typically do not add crossing_ref=zebra as all pedestrian crossing here are "zebras". We do not have the other types. BTW, the <a href="https://wiki.openstreetmap.org/wiki/Key:crossing">crossing</a> wiki page does not mention crossing=zebra at all.</p>
</div>
<div id="comment-44086-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 20:02)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44089"></span>
<div id="comment-44089" class="comment not_top_scorer">
<div id="post-44089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting. Currently <a href="http://taginfo.openstreetmap.org/keys/crossing#values">crossing=zebra is the third most crossing tag</a>.</p>
</div>
<div id="comment-44089-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 20:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44092"></span>
<div id="comment-44092" class="comment not_top_scorer">
<div id="post-44092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The crossing = zebra perhaps a reference to the white lines (in Brazil the default is one) where the pedestrian pass.</p>
<p>So I do like this: highway = crossing with crossing = traffic_signals? At the same point (node)?</p>
<p>If so, how to add the rcossing = zebra? ... Considering that he needed to determine the type of pass (zebra)?</p>
</div>
<div id="comment-44092-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 23:05)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44093"></span>
<div id="comment-44093" class="comment not_top_scorer">
<div id="post-44093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See the page on <a href="https://wiki.openstreetmap.org/wiki/Key:crossing">crossing</a>, use crossing_ref : "The traditional, region-specific reference, such as zebra or pelican"</p>
</div>
<div id="comment-44093-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 04:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44097"></span>
<div id="comment-44097" class="comment not_top_scorer">
<div id="post-44097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I still don't understand why you want to add crossing=traffic_signals <em>and</em> cossing=zebra. Either there are traffic signals <em>for pedestrians</em>. Or there are none in which case there might still be other markings as for example zebra stripes.</p>
</div>
<div id="comment-44097-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 07:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44103"></span>
<div id="comment-44103" class="comment not_top_scorer">
<div id="post-44103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I will detail best.</p>
<p>I use the iD editor. In point (node) are two different elements: the passage of pedestrians and the traffic signal for the cars.</p>
<p>I need to add these two elements in the same place, right?</p>
<p>When I add the element = highway crossing, the iD editor already assigns it the crossing = zebra. The point is this: highway = crossing with cossing = zebra.</p>
<p>See who still lack even the highway = raffic_signals. How to add it is my doubt.</p>
<p>Therefore, the title of the question I proposed this: highway = crossing with highway_1 = traffic_signals.</p>
<p>Explain to me how to do this, since the iD editor, by default, will define the first point thus: highway = crossing with cossing = zebra.</p>
</div>
<div id="comment-44103-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 11:30)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44104"></span>
<div id="comment-44104" class="comment">
<div id="post-44104-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You don't have to add pedestrian and car traffic signals in the same place, it is perfectly fine to use separate positions and thus separate nodes for them. In case you want to add both using the same node then use highway=traffic_signals and crossing=traffic_signals as stated by escada.</p>
<p>I can confirm that iD automatically adds crossing=zebra if you select to add a crosswalk. This is indeed questionable. But you can still change it afterwards. Either by selecting "traffic signals" from the list of types. Or by going to "All tags" and changing it manually to crossing=traffic_signals.</p>
</div>
<div id="comment-44104-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 12:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44108"></span>
<div id="comment-44108" class="comment not_top_scorer">
<div id="post-44108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Scai ... but the traffic signal (for cars) is exactly through which pedestrians.</p>
<p>I did what you suggested: putting different points. Maybe it's the tits out, but I believe that should be at the same point.</p>
<p>Here's a link the intersection in question. analyze and see if it's correct:</p>
<p><a href="https://www.openstreetmap.org/edit?node=3641052960#map=20/-20.46169/-54.61949">https://www.openstreetmap.org/edit?node=3641052960#map=20/-20.46169/-54.61949</a></p>
<p>For e.s.c.a.d.a .: I think this complicated issue. I think he should really be better debated, to define a common standard to everyone, which is difficult. I do not use the JOSM because it is incompatible with Chromebooks.</p>
<p>Here's a link the intersection in question. analyze and see if it's correct: <a href="https://www.openstreetmap.org/edit?node=3641052960#map=20/-20.46169/-54.61949">https://www.openstreetmap.org/edit?node=3641052960#map=20/-20.46169/-54.61949</a></p>
</div>
<div id="comment-44108-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 13:08)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="44112"></span>
<div id="comment-44112" class="comment">
<div id="post-44112-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please read my previous comment again. It is <em>possible</em> to add both at the same node, you don't have to use different positions. But you <em>can</em> if you want to. As explained by escada this may even improve accuracy if the traffic signals are at a crossing.</p>
</div>
<div id="comment-44112-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 13:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44113"></span>
<div id="comment-44113" class="comment">
<div id="post-44113-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, now I understand. I will do so: highway = crossing, crossing = traffic_signals, crossing_ref = zebra, which is what actually occurs at the intersection.</p>
<p>The highway = traffic_signals (as escada- suggested) at the intersection of routes as a single signal, do not think that is the most correct because the intersection has two signals.</p>
<p>Thank you for your patience.</p>
</div>
<div id="comment-44113-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 14:02)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
</div>
<div id="comment-tools-44047" class="comment-tools">
<span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44047-form-container" class="comment-form-container">
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

