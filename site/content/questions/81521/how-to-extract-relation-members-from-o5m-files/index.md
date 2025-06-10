+++
type = "question"
title = "How to extract relation members from .o5m files"
description = '''Edit: An update, I&#x27;ll put it at the top because it is most relevant now: I made some progress. When I use the following code: import osmium as osm import pandas as pd  class OSMHandler(osm.SimpleHandler):  def __init__(self):  osm.SimpleHandler.__init__(self)  self.osm_data = []   def tag_inventory(...'''
date = "2021-08-28T21:52:00Z"
lastmod = "2021-11-14T15:25:00Z"
weight = 81521
keywords = [ "mtb", "o5m", "relations", "pyosmium" ]
aliases = [ "/questions/81521" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract relation members from .o5m files](/questions/81521/how-to-extract-relation-members-from-o5m-files)

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
<span id="post-81521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Edit: An update, I'll put it at the top because it is most relevant now:</p>
<p>I made some progress.</p>
<p>When I use the following code:</p>
<pre><code>import osmium as osm
import pandas as pd
&#10;class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []
&#10;    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            if elem_type == &#39;relation&#39;:
                members = elem.members
            else:
                members = &#39;None&#39;
&#10;            self.osm_data.append([elem_type, 
                               elem.id, 
                               elem.version,
                               elem.visible,
                               pd.Timestamp(elem.timestamp),
                               elem.uid,
                               elem.user,
                               elem.changeset,
                               len(elem.tags),
                               tag.k, 
                               tag.v,
                               members
                               ])
&#10;
    def node(self, n):
        self.tag_inventory(n, &quot;node&quot;)
&#10;    def way(self, w):
        self.tag_inventory(w, &quot;way&quot;)
&#10;    def relation(self, r):
        self.tag_inventory(r, &quot;relation&quot;)
&#10;osmhandler = OSMHandler()
osmhandler.apply_file(&quot;../data/world_mtb_routes.o5m&quot;)</code></pre>
<p>I get the error:</p>
<pre><code>RuntimeError: Relation callback keeps reference to OSM object. This is not allowed.</code></pre>
<p>Strangely if I just use:</p>
<pre><code>if elem_type == &#39;relation&#39;:
    print(elem.members)</code></pre>
<p>Instead of trying to add the the info to self.osm_data, I do see the information I want scrolling by!</p>
<p>What am I missing? Why can I add elem.id etc to the self.osm_data but not elem.members?</p>
<p>====&gt; The original question:</p>
<p>All,</p>
<p>I've been trying to build a website (in Django) which is to be an index of all MTB routes in the world. I'm a Pythonian so wherever I can I try to use Python.</p>
<p>I've successfully extracted data from the OSM API (<a href="https://stackoverflow.com/questions/68248846/display-relation-trail-in-leaflet">Display relation (trail) in leaflet</a>) but found that doing this for all MTB trails (tag: route=mtb) is too much data (processing takes very long). So I tried to do everything locally by downloading a torrent of the entire OpenStreetMap dataset (from planet.openstreetmap.org]<a href="https://stackoverflow.com/questions/45771809/how-to-extract-and-visualize-data-from-osm-file-in-python">2</a>), converted the osm file to o5m, and filtering for tag: route=mtb using osmfilter (part of osmctools in Ubuntu 20.04), like this:</p>
<pre><code>osmfilter $unzipped_osm_planet_file --keep=&quot;route=mtb&quot; -o=$osm_planet_dir/world_mtb_routes.o5m</code></pre>
<p>This produces a file of about 83.6 MB and on closer inspection seems to contain all the data I need. My goal was to transform the file into a pandas.DataFrame() so I could do some further filtering en transforming before pushing relevant aspects into my Django DB. I tried to load the file as a regular XML file using Python Pandas but this crashed the Jupyter notebook Kernel. I guess the data is too big.</p>
<p>My second approach was this solution: <a href="https://stackoverflow.com/questions/45771809/how-to-extract-and-visualize-data-from-osm-file-in-python">How to extract and visualize data from OSM file in Python</a>. It worked for me, at least, I can get some of the information, like the tags of the relations in the file (and the other specified details). What I'm missing is the relation members (the ways) and then the way members (the nodes) and their latitude/longitudes. I need these to achieve what I did here: <a href="https://stackoverflow.com/questions/68375034/plotting-openstreetmap-relations-does-not-generate-continous-lines">Plotting OpenStreetMap relations does not generate continuous lines</a>.</p>
<p>I'm open to many solutions, at the moment I feel that I don't understand how pyosmium works, but I must be close. Any help is appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mtb" rel="tag" title="see questions tagged &#39;mtb&#39;">mtb</span> <span class="post-tag tag-link-o5m" rel="tag" title="see questions tagged &#39;o5m&#39;">o5m</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-pyosmium" rel="tag" title="see questions tagged &#39;pyosmium&#39;">pyosmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '21, 21:52</strong></p>
<img src="https://secure.gravatar.com/avatar/1581be81998cfdcc55dd8d43194aca23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FreekvH&#39;s gravatar image" />
<p><span>FreekvH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FreekvH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '21, 09:08</strong> </span></p>
</div>
</div>
<div id="comments-container-81521" class="comments-container">
&#10;</div>
<div id="comment-tools-81521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81521-form-container" class="comment-form-container">
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

<span id="81538"></span>

<div id="answer-container-81538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81538-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>pyosmium gives you only a temporary view of the data from the file. This makes processing fast because it avoids unnecessary copying but it means that you have to make a <strong>deep</strong> copy of any data you want to keep. The <code>id</code> field is just an integer, so assigning it to another variable gives you the full deep copy. <code>members</code> is an array which needs to be copied explicitly:</p>
<pre><code>members = [(m.type, m.ref, m.role) for m in elem.members]</code></pre>
<p>The same is true for the tag list (<code>elem.tags</code>). As a rule: don't just blindly copy all information you can get. Just keep what you really need later.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '21, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-81538" class="comments-container">
<span id="81540"></span>
<div id="comment-81540" class="comment">
<div id="post-81540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this works! I didn't realize there was a difference in "id" and "members". Thanx a million!</p>
<p>I will make my code complete and indeed make it more minimal (I just need a dict with some values, like data[relation][ways][nodes] and some meta data, I'll post my final version here when it works.</p>
</div>
<div id="comment-81540-info" class="comment-info">
<span class="comment-age">(29 Aug '21, 17:35)</span> <span class="comment-user userinfo">FreekvH</span>
</div>
</div>
</div>
<div id="comment-tools-81538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81538-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82567"></span>

<div id="answer-container-82567" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have finally solved this, I posted the answer on stackoverlow, I'll link to it here because then I have one place to update.</p>
<p>The answer: <a href="https://stackoverflow.com/questions/68622198/how-to-extract-relation-members-from-osm-xml-files">stackoverflow.com/questions/68622198/how-to-extract-relation-members-from-osm-xml-files</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '21, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/1581be81998cfdcc55dd8d43194aca23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FreekvH&#39;s gravatar image" />
<p><span>FreekvH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FreekvH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '21, 15:26</strong> </span></p>
</div>
</div>
<div id="comments-container-82567" class="comments-container">
&#10;</div>
<div id="comment-tools-82567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82567-form-container" class="comment-form-container">
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

