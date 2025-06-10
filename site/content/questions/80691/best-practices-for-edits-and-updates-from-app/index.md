+++
type = "question"
title = "Best practices for edits and updates from App"
description = '''Hello everyone,  We are developing an app for bar, hotel and restaurant reviews, called Revuie. With all the changes that have happened with hospitality recently, we need to be able to give our users a quick and easy way to edit or add venues. Hopefully, we can add back by contributing those edits. ...'''
date = "2021-06-24T15:11:00Z"
lastmod = "2021-06-28T12:18:00Z"
weight = 80691
keywords = [ "editing", "api", "tagging" ]
aliases = [ "/questions/80691" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best practices for edits and updates from App](/questions/80691/best-practices-for-edits-and-updates-from-app)

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
<span id="post-80691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80691-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>We are developing an app for bar, hotel and restaurant reviews, called Revuie.</p>
<p>With all the changes that have happened with hospitality recently, we need to be able to give our users a quick and easy way to edit or add venues. Hopefully, we can add back by contributing those edits. But we’re wary of the risk of bad edits.</p>
<p>One initial idea was to just make the edits in our local data, and then publish a change file that could be used as a source for the community. But the problem we can’t get our heads around is how to de-dupe those changes on future imports of OSM data.</p>
<p>Another alternative is to use the API to make the changes, identifying them as coming from a user tied to our app - and maybe setting them as needing review?</p>
<p>Whatever approach we take, we can create guides for users so that they can get a feel for how and when to make edits - and as the change functionality is implemented in the app it can be buttoned down.</p>
<p>We’d love to be a part of the community, and to contribute it back, so it would be great to get any advice and feedback people have on this, please.</p>
<p>Another puzzle we're facing is how to enable users to tag venues, and keep that tag list in line with existing OSM tags, as the tags could come from various sources. For example, we'd definitely want to include cuisine. Some pubs have sport tags (like pool) which could be useful. Across food, drink and accommodation, there must be lots of tags that we haven't considered. Any advice on this would be great too. Ultimately, we want to encourage tagging of venues in the app to enhance user search, and it would be great to contribute this back too.</p>
<p>Many thanks,</p>
<p>John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '21, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/8f3e7fb1eed3f0aa42bdbc129500d31b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnB-Revuie&#39;s gravatar image" />
<p><span>JohnB-Revuie</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnB-Revuie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '21, 08:21</strong> </span></p>
</div>
</div>
<div id="comments-container-80691" class="comments-container">
&#10;</div>
<div id="comment-tools-80691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80691-form-container" class="comment-form-container">
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

<span id="80718"></span>

<div id="answer-container-80718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80718-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi John, it sounds like you have two possible approaches here:</p>
<ul>
<li>Include limited OSM editing capability as a feature of your app, calling the API directly from users' devices. Many apps do this; OsmAnd is probably the most prominent. Any user of your app who wished to contribute data to OSM would need to create an OSM account, and supply your app with their credentials.</li>
<li>Collect and curate data from your users into your own database, and import that data into OSM at intervals using a single dedicated OSM account. As you mention, there's the obvious problem of deduplication. Also, imports in general are a tricky topic, and there have been many over the years that have done a lot of damage, so prepare for a lot of resistance to this approach.</li>
</ul>
<p>Some useful reading:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Organised_Editing_Guidelines">https://wiki.openstreetmap.org/wiki/Organised_Editing_Guidelines</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a></li>
</ul>
<p>Regarding the tagging, you'll want to maintain parity with existing OSM tagging practices. There are established tags for cuisine, for indicating that pub has a pool table, etc. There may, though, be details that you're interested in that are considered out of scope for OSM, such as individual menu items, pricing information, special promotions, government inspection scores, and, of course, the reviews and ratings themselves.</p>
<p>...</p>
<p>Whenever I hear of third-party apps using OSM for business reviews, the biggest problem that comes to mind is that there is no standard method to ensure that an individual business has a persistent unique ID in OSM. Eg, one mapper might add a restaurant as a node, then another mapper might remap it as a building, which will be a different element in the OSM database. Then another mapper might decide it shouldn't be the whole building because it's a multi story building and the restaurant is only on the ground floor, so it gets moved to a brand new node inside the building.</p>
<p>Then the restaurant moves into a new building across the street. A mapper might choose to move the node from the old building to the new one... or to create a new node in the new building, and change the tags on the old node so it's reused for the new business that's moved into the old space.</p>
<p>Meanwhile, the name might change, eg "Greggorys"-&gt;"Greggory's"-&gt;"Gregory's"-&gt;"Gregory's Cafe". The phone number and website might change too. It would take a fair amount of work to sync a single record in a remote database with these different OSM elements and changing tag values.</p>
<p>This is a solvable problem, but be aware that it will happen.</p>
<p>Some more fun reading: <a href="https://wiki.openstreetmap.org/wiki/Persistent_Place_Identifier">https://wiki.openstreetmap.org/wiki/Persistent_Place_Identifier</a></p>
<p>Good luck with your app!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '21, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '21, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-80718" class="comments-container">
<span id="80723"></span>
<div id="comment-80723" class="comment not_top_scorer">
<div id="post-80723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi jmapb, thanks for the detailed answer.</p>
<p>With the editing, I wonder if there is an in between option, where we call the API for limited editing, but use a 'RevuieApp' OSM account, so the user doesn't have to create their own. This would also mean that any edits could be easily identified as coming from the app, so we could more easily tweak the process in the app based on feedback from the community. Would be great to hear any thoughts on that.</p>
<p>Thanks for the tip on the persistent unique ID. We hadn't accounted for that, so will read up on the links and put some thought in to it. I'm sure we'll be back with more questions on that one!</p>
<p>Thanks again,</p>
<p>John</p>
</div>
<div id="comment-80723-info" class="comment-info">
<span class="comment-age">(26 Jun '21, 10:34)</span> <span class="comment-user userinfo">JohnB-Revuie</span>
</div>
</div>
<span id="80724"></span>
<div id="comment-80724" class="comment">
<div id="post-80724-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you are creating a new app that submits edits it should already have a <a href="https://wiki.openstreetmap.org/wiki/Key:created%20by?uselang=en"><code>created_by</code></a> tag set on the changeset to make them identifiable regardless.</p>
</div>
<div id="comment-80724-info" class="comment-info">
<span class="comment-age">(26 Jun '21, 13:51)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80748"></span>
<div id="comment-80748" class="comment not_top_scorer">
<div id="post-80748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks InsertUser, will have a look at that tag</p>
</div>
<div id="comment-80748-info" class="comment-info">
<span class="comment-age">(27 Jun '21, 19:24)</span> <span class="comment-user userinfo">JohnB-Revuie</span>
</div>
</div>
<span id="80750"></span>
<div id="comment-80750" class="comment">
<div id="post-80750-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>On the question of using a "'RevuieApp' OSM account", I suspect that you might struggle to agree to OSM's <a href="https://wiki.osmfoundation.org/wiki/Licence/Contributor_Terms">Contributor Terms</a> given that you don't know what users are submitting or where they've got it from. Generally speaking apps use one account per actual user. There's an OSM <a href="https://wiki.osmfoundation.org/wiki/Licensing_Working_Group">Licensing Working Group</a> and they'd have more idea than me.</p>
</div>
<div id="comment-80750-info" class="comment-info">
<span class="comment-age">(27 Jun '21, 22:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80755"></span>
<div id="comment-80755" class="comment">
<div id="post-80755-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20411/johnb-revuie">@JohnB-Revuie</a> I can't speak for anyone but myself as an OSM mapper and user, but offhand... numerous users editing the map with a shared account doesn't sound like a good idea.</p>
<p>By design, individual users are responsible for their own changes to the map, and other users may want to communicate with them about those changes. If I see a change I don't understand or wish to know more about, I can leave a comment on the changeset, or message the user directly. This will trigger an email to the address associated with the account.</p>
<p>Whoever handles your RevuieApp account would get emails intended for the users who actually made the changes, eg "Why did you call this a doctor? It looks like a deli" or "Are you sure they're open? I passed by last week and it had a For Rent sign" or "Did Gregory's close, or is this another business in the same building?" or "Why did you change this to a restaurant?" These questions might make sense to the user who made the change, but not to whoever's checking the email account for the RevuieApp OSM user.</p>
</div>
<div id="comment-80755-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 02:19)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="80756"></span>
<div id="comment-80756" class="comment">
<div id="post-80756-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20411/johnb-revuie">@JohnB-Revuie</a> Also, if one of your users was suspected of copyright infringement or vandalism, OSM's Data Working Group would get complaints against the entire RevuieApp account, and might choose the block all of this account's access, which would break the app for everyone.</p>
<p>In short, what you're describing is different enough from the way that OSM usually works that I don't think it would go over well, and I wouldn't be surprised if it was somehow explicitly forbidden.</p>
</div>
<div id="comment-80756-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 02:21)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="80759"></span>
<div id="comment-80759" class="comment">
<div id="post-80759-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks jmapb and SomeoneElse. Some really key points for us to think about there, especially around the contributor terms and the risk to the whole account being blocked.</p>
</div>
<div id="comment-80759-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 12:18)</span> <span class="comment-user userinfo">JohnB-Revuie</span>
</div>
</div>
</div>
<div id="comment-tools-80718" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-80718-form-container" class="comment-form-container">
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

