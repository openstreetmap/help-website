+++
type = "question"
title = "Extract street names with all boundaries that its belong to"
description = '''Hi, I have to extract all street names with all boundaries that its belong to. I found webpage https://osm-boundaries.com/ where you can select a lot of boundaries. eg. Germany -&amp;gt; Baden-Wurttemberg -&amp;gt; Regierungsbezirk -&amp;gt; Freiburg im Breisgau -&amp;gt; Altstadt -&amp;gt; Altstadt-Mitte Now im in the...'''
date = "2020-12-29T12:42:00Z"
lastmod = "2021-01-04T08:05:00Z"
weight = 78101
keywords = [ "boundaries", "boundary", "streetnames", "streetname" ]
aliases = [ "/questions/78101" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract street names with all boundaries that its belong to](/questions/78101/extract-street-names-with-all-boundaries-that-its-belong-to)

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
<span id="post-78101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78101-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have to extract all street names with all boundaries that its belong to. I found webpage <a href="https://osm-boundaries.com/">https://osm-boundaries.com/</a> where you can select a lot of boundaries. eg. Germany -&gt; Baden-Wurttemberg -&gt; Regierungsbezirk -&gt; Freiburg im Breisgau -&gt; Altstadt -&gt; Altstadt-Mitte Now im in the point that i can extract all street names (Type=Way, contain tag highway, contain name) Is it possible to extract all boundary names for each street ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-streetname" rel="tag" title="see questions tagged &#39;streetname&#39;">streetname</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '20, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/b67f3bd21032c36825f2da5fb110223b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HubDac&#39;s gravatar image" />
<p><span>HubDac</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HubDac has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78101" class="comments-container">
<span id="78117"></span>
<div id="comment-78117" class="comment">
<div id="post-78117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using OsmSharp i wrote some code but it seems to not working as i expected :( But i dont know why :(</p>
<p>The funniest part is that there are some relations that eg.</p>
<blockquote>
<p>&lt;waynode&gt; &lt;city/&gt; &lt;name&gt;Otto-Reutter-Straße&lt;/name&gt; &lt;type&gt;residential&lt;/type&gt; &lt;areas&gt; &lt;arearelation&gt; &lt;nodeid&gt;430112483&lt;/nodeid&gt; &lt;name&gt;Dotzheim&lt;/name&gt; &lt;type&gt;boundary&lt;/type&gt; &lt;boundary&gt;administrative&lt;/boundary&gt; &lt;adminlevel&gt;9&lt;/adminlevel&gt; &lt;/arearelation&gt; &lt;arearelation&gt; &lt;nodeid&gt;430112483&lt;/nodeid&gt; &lt;name&gt;Schierstein&lt;/name&gt; &lt;type&gt;boundary&lt;/type&gt; &lt;boundary&gt;administrative&lt;/boundary&gt; &lt;adminlevel&gt;9&lt;/adminlevel&gt; &lt;/arearelation&gt; &lt;/areas&gt; &lt;/waynode&gt;</p>
</blockquote>
<p>but i most cases (output xml contains 16.868.559 lines of text) Ways(count 3.369.198) are not connected in Relation(count 2.818) whole file contain: Nodes: 331.798.468 Ways: 54.132.981 Relations: 666.231 and i dont use Node's at all at current implementation.</p>
<pre><code>using (var fileStream = File.OpenRead(@&quot;.\germany-latest.osm.pbf&quot;))
        {
            // create source stream.
            var source = new PBFOsmStreamSource(fileStream);
&#10;            var relationNodes = source
                .Where(w =&gt; 
                    w.Type == OsmGeoType.Relation
                    &amp;&amp; w.Tags.ContainsKey(&quot;boundary&quot;)
                    &amp;&amp; w.Tags.ContainsKey(&quot;admin_level&quot;))
                .SelectMany(s =&gt; (s as Relation)?.Members
                            .Where(wm =&gt; wm.Type == OsmGeoType.Way)
                            .Select(sm =&gt; new AreaRelation()
                            {
                                NodeId = sm.Id,
                                Name = s.Tags.GetValue(&quot;name&quot;),
                                Type = s.Tags.GetValue(&quot;type&quot;),
                                Boundary = s.Tags.GetValue(&quot;boundary&quot;),
                                AdminLevel = s.Tags.GetValue(&quot;admin_level&quot;)
                            })
                            .OrderBy(o =&gt; o.AdminLevel))
                .ToList();
&#10;            var relationNodesGroupedByNodeId = relationNodes.GroupBy(k =&gt; k.NodeId, v =&gt; v).ToDictionary(k =&gt; k.Key, v =&gt; v);
&#10;            var wayNodes = source
                .Where(w =&gt;
                    w.Type == OsmGeoType.Way
                    &amp;&amp; w.Tags.ContainsKey(&quot;highway&quot;)
                    &amp;&amp; w.Tags.ContainsKey(&quot;name&quot;))
                .Select(s =&gt;
                    new WayNode()
                    {
                        City = s.Tags.GetValue(&quot;is_in:city&quot;),
                        Name = s.Tags.GetValue(&quot;name&quot;),
                        Type = s.Tags.GetValue(&quot;highway&quot;),
                        Areas = (s.Id.HasValue &amp;&amp; relationNodesGroupedByNodeId.ContainsKey(s.Id.Value)) 
                            ? relationNodesGroupedByNodeId[s.Id.Value].ToList() 
                            : null
                    })
                .Distinct().ToList();
&#10;            XmlSerializer x = new XmlSerializer(wayNodes.GetType());
&#10;            var path = @&quot;.\GermanyWays2.xml&quot;;
            FileStream file = System.IO.File.Create(path);
&#10;            x.Serialize(file, wayNodes);
            file.Close();
}</code></pre>
</div>
<div id="comment-78117-info" class="comment-info">
<span class="comment-age">(30 Dec '20, 08:09)</span> <span class="comment-user userinfo">HubDac</span>
</div>
</div>
<span id="78125"></span>
<div id="comment-78125" class="comment">
<div id="post-78125-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What are you actually trying to accomplish?</p>
</div>
<div id="comment-78125-info" class="comment-info">
<span class="comment-age">(30 Dec '20, 13:39)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="78220"></span>
<div id="comment-78220" class="comment">
<div id="post-78220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to extract all streets for Germany with their administration bouderies. So if street is in Berlin i have to get street name and collection of areas e.g. level 2: Germany level 4: Berlin level 9: Mitte level 10: Moabit (i took areas names and leves from www.osm-boundaries.com)</p>
</div>
<div id="comment-78220-info" class="comment-info">
<span class="comment-age">(04 Jan '21, 08:05)</span> <span class="comment-user userinfo">HubDac</span>
</div>
</div>
</div>
<div id="comment-tools-78101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78101-form-container" class="comment-form-container">
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

<span id="78120"></span>

<div id="answer-container-78120" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I have a relation that includes the tags "boundary" and "admin_level", do the members of that relationship form a polygon? and everything inside that polygon should basically be treated as if it had these markers?</p>
<h1 id="edit">EDIT</h1>
<p>I also noticed that there are relation members of type "Node" with Id that does not exists. The Id of node from relation member does not exists as id of any Node :(</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '20, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b67f3bd21032c36825f2da5fb110223b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HubDac&#39;s gravatar image" />
<p><span>HubDac</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HubDac has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '20, 10:42</strong> </span></p>
</div>
</div>
<div id="comments-container-78120" class="comments-container">
&#10;</div>
<div id="comment-tools-78120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78120-form-container" class="comment-form-container">
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

