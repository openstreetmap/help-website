+++
type = "question"
title = "Apple App &#x27;Go Map!!&#x27;: Error when uploading the change sets"
description = '''Hello, just noticed that many of my edits in the app &#x27;Go Map!!!&#x27; cannot be uploaded. The error message appears: &quot;Cannot upload changes Version mismatch: Provider 1, server had: 2 of Node 8784766722 POST https://api.openstreetmap.org/api/0.6/c ... 220/upload The &quot;raw XML data&quot; can be edited in the &#x27;G...'''
date = "2021-06-06T06:33:00Z"
lastmod = "2021-06-07T20:38:00Z"
weight = 80426
keywords = [ "apple_gomap" ]
aliases = [ "/questions/80426" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Apple App 'Go Map!!': Error when uploading the change sets](/questions/80426/apple-app-go-map-error-when-uploading-the-change-sets)

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
<span id="post-80426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80426-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, just noticed that many of my edits in the app 'Go Map!!!' cannot be uploaded. The error message appears: "Cannot upload changes</p>
<p>Version mismatch: Provider 1, server had: 2 of Node 8784766722</p>
<p>POST <a href="https://api.openstreetmap.org/api/0.6/c">https://api.openstreetmap.org/api/0.6/c</a> ... 220/upload</p>
<p>The "raw XML data" can be edited in the 'Go Map!!!' app to "fix errors that prevent uploading." I don't know how though, Can delete and write there.</p>
<p>Maybe someone has a tip?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apple_gomap" rel="tag" title="see questions tagged &#39;apple_gomap&#39;">apple_gomap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '21, 06:33</strong></p>
<img src="https://secure.gravatar.com/avatar/7a9cd72fa3e8d977ead0aa0dcb364884?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ingolf2&#39;s gravatar image" />
<p><span>Ingolf2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ingolf2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80426" class="comments-container">
<span id="80427"></span>
<div id="comment-80427" class="comment">
<div id="post-80427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I go to the link, the error message appears: "This page does not work"</p>
<p>If you try again, the error message changes: The upper text remains the same, it changes: "POST <a href="https://api.openstreetmap.org/api/0.6/c">https://api.openstreetmap.org/api/0.6/c</a> ... 431/upload "</p>
<p>The OSM app 'Go Map!!' is an Apple app, that is actually a joy to use.</p>
</div>
<div id="comment-80427-info" class="comment-info">
<span class="comment-age">(06 Jun '21, 06:47)</span> <span class="comment-user userinfo">Ingolf2</span>
</div>
</div>
</div>
<div id="comment-tools-80426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80426-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="80428"></span>

<div id="answer-container-80428" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80428-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error seems to be a simple version conflict, to fix it you either need to not upload the element in question or, increase the version number to 2.</p>
<p>The former makes sense if your changes are incompatible (that is for example different, incompatible, tagging).</p>
<p>A simple text editor should be enough to do this, <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">https://wiki.openstreetmap.org/wiki/OSM_XML</a> gives some information on the XML format. Likely your edits are not in the normal XML format but in the <a href="https://wiki.openstreetmap.org/wiki/OsmChange">https://wiki.openstreetmap.org/wiki/OsmChange</a> format which just contains the changes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '21, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-80428" class="comments-container">
<span id="80433"></span>
<div id="comment-80433" class="comment">
<div id="post-80433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does <em>Go Map!!</em> have an "Update data" option like Vespucci or JOSM?</p>
</div>
<div id="comment-80433-info" class="comment-info">
<span class="comment-age">(06 Jun '21, 17:32)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80436"></span>
<div id="comment-80436" class="comment">
<div id="post-80436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can refresh GoMap!!'s OSM data under the "Display" menu (folded map icon on the right), under the "Clear Cache" submenu. Here you can select "Clear OSM Data" and then the map data will reload as needed when you browse the map. This will destroy any unsaved changes though. It's not possible to reload and preserve any unconflicting changes.</p>
</div>
<div id="comment-80436-info" class="comment-info">
<span class="comment-age">(06 Jun '21, 18:59)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-80428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80428-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80435"></span>

<div id="answer-container-80435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80435-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems you're attempting to use GoMap!!'s pre-upload changeset edit mode to resolve this conflict. That might work. As Simon says, you'd need to locate the XML element for the node in question, and either increase the version number (so you'll be overwriting the changes made in the previous version) or remove that entire node element from the changeset (so you'll be losing the changes you made to this node in GoMap!! and keeping the current OSM version.)</p>
<p>The problem is that editing the raw XML on a small touchscreen can be difficult, especially if you have over a hundred changes in that changeset. But if you're careful, you'll be able to scroll through and find the XML code for the correct node ID. Increasing the version number would probably be the easier approach, since it's a much smaller edit than deleting the whole node element. Normally I'd be wary about overwriting other mapper's changes but it looks like you're the one who actually made the change in the meantime, adding wheelchair=yes via StreetComplete, so overwriting probably wouldn't be a big problem. The wheelchair=yes tag would presumably survive, but if not you could fix it later.</p>
<p>GoMap!! can also email the changeset to you as an attachment. You could then examine it using a text editor on a desktop computer, which might help you find the spot that needs changed. You could even make the changes on the computer and email the changed file back to the phone, then try to copy and paste that changed version into GoMap!!'s edit screen.</p>
<p>You could also take the emailed changeset file and load it into <a href="https://josm.openstreetmap.de/">JOSM</a>, a desktop map editor. But JOSM has a steep learning curve so if you've never used it before that's a pretty daunting approach too. Another alternative might be <a href="http://level0.osmz.ru">Level0</a>, a simplefied low-level OSM data editor where you could upload the modified changeset file and then commit it to the database. It's not particularly user-friendly either, though.</p>
<p>Good luck, J</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '21, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '21, 00:44</strong> </span></p>
</div>
</div>
<div id="comments-container-80435" class="comments-container">
<span id="80441"></span>
<div id="comment-80441" class="comment">
<div id="post-80441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM may have a 'steep' learning curve, but it's nothing compared to hand editing OSM XML. JOSM's <a href="https://learnosm.org/en/josm/josm-conflict-resolution/">conflict resolution</a> could be better for complex things, but from the sound of it, this conflict shouldn't be too difficult.</p>
</div>
<div id="comment-80441-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 05:20)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80454"></span>
<div id="comment-80454" class="comment">
<div id="post-80454-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Depends on the person I guess -- XML is familiar to millions. But yes, it's very easy to break, especially on a small touchscreen with no syntax validation.</p>
<p>I remembered that Level0 can load the same changeset files that GoMap!! exports by email, and I edited my answer to include that option. That's probably the easiest way, assuming that additional conflicts haven't arisen in the meantime.</p>
<p>I agree that using JOSM would be the "right" way to do it.</p>
</div>
<div id="comment-80454-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 13:16)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-80435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80435-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80429"></span>

<div id="answer-container-80429" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80429-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your detailed message.</p>
<p>I think it is clearly my fault. In app are 101 edits of nodes to upload. This can not do the app, the phone. I am using the app for the first time and thought it would work without the 'upload button'. It was late at night and I was under the impression.</p>
<p>I will delete many nodes now, after a copy of all the text.</p>
<p>But how do I delete correctly?? E.G.:</p>
<p>" &lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;osmchange generator="Go Map!! 2.2.1" version="0.6"&gt; &lt;create&gt; &lt;node id="-5" timestamp="2021-06-05T22:24:08Z" version="1" lat="51.57168009376723" lon="8.105626210283127"&gt; &lt;tag k="tourism" v="information"&gt;&lt;/tag&gt; &lt;tag k="information" v="aus Kupfer, im Plaster, Mittelpunkt der Stadt Soest"&gt;&lt;/tag&gt; &lt;tag k="name" v="Koordinatenkreuz"&gt;&lt;/tag&gt; &lt;tag k="operator" v="Stadt Soest"&gt;&lt;/tag&gt; &lt;/node&gt; &lt;node id="-4" timestamp="2021-06-05T22:04:09Z" version="1" lat="51.57272165414511" lon="8.106468646334125"&gt; &lt;tag k="tourism" v="information"&gt;&lt;/tag&gt; &lt;tag k="religion" v="Kontur im Pflaster sichtbar. In der Mitte befand sich ein hölzerner Pfahl."&gt;&lt;/tag&gt; &lt;tag k="information" v="Konturen im Pflaster erkennbar, in der Mitte stand ein Holzpfahl"&gt;&lt;/tag&gt; &lt;tag k="name" v="Pranger"&gt;&lt;/tag&gt; &lt;tag k="operator" v="Stadt Soest"&gt;&lt;/tag&gt; &lt;/node&gt; &lt;/create&gt; &lt;modify&gt; &lt;node id="4090388674" timestamp="2016-04-01T17:35:13Z" version="1" lat="51.5704817" lon="8.109112400000001"&gt;</p>
<pre><code>  &lt;tag k=&quot;phone&quot; v=&quot;+49 2921 16380&quot;&gt;&lt;/tag&gt;
  &lt;tag k=&quot;shop&quot; v=&quot;tailor&quot;&gt;&lt;/tag&gt;
  &lt;tag k=&quot;name&quot; v=&quot;Jakob&#39;s Änderungsschneiderei&quot;&gt;&lt;/tag&gt;
  &lt;tag k=&quot;stroller&quot; v=&quot;yes&quot;&gt;&lt;/tag&gt;</code></pre>
<p>Now, in this example, if I want to delete the node "4090388674", would I have to delete up to and including &lt;/node&gt; , above it?</p>
<p>If I then want to delete the node "-4", would I then have to delete up to and including &lt;/node&gt; , above it, again?</p>
<p>How many nodes can the app, the phone: iPhone 6 plus, probably upload at once?</p>
<p>Thanks for an answer.</p>
<p>I'm annoyed with myself for not uploading in between.</p>
<p>But this way I learn something.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '21, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/7a9cd72fa3e8d977ead0aa0dcb364884?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ingolf2&#39;s gravatar image" />
<p><span>Ingolf2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ingolf2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '21, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-80429" class="comments-container">
<span id="80462"></span>
<div id="comment-80462" class="comment">
<div id="post-80462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you wish to delete the node id="-4" then you'd need to start at: <code>&lt;node id="-4" timestamp="2021-06-05T22:04:09Z"</code> and end at <code>v="Stadt Soest"&gt;&lt;/tag&gt; &lt;/node&gt;</code> with all of the text in between.</p>
</div>
<div id="comment-80462-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 20:38)</span> <span class="comment-user userinfo">atom oil</span>
</div>
</div>
</div>
<div id="comment-tools-80429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80429-form-container" class="comment-form-container">
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

