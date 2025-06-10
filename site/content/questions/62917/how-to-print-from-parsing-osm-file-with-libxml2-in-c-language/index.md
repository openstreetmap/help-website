+++
type = "question"
title = "[closed] How to print from parsing .osm file with libxml2 in C language"
description = '''I&#x27;m working on XML file (in particula .osm file) with libxml2 and C language. This is my XML source (not all but just a piece): ...  &amp;lt; way id=&quot;9484424&quot; visible=&quot;true&quot; version=&quot;8&quot; changeset=&quot;11179686&quot; timestamp=&quot;2012-04-04T18:01:31Z&quot; user=&quot;Davlak&quot; uid=&quot;217070&quot;&amp;gt;  &amp;lt; nd ref=&quot;72843570&quot;/&amp;gt;  &amp;lt...'''
date = "2018-04-05T11:14:00Z"
lastmod = "2018-04-05T11:14:00Z"
weight = 62917
keywords = [ "libxml2", ".osm", "printf" ]
aliases = [ "/questions/62917" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to print from parsing .osm file with libxml2 in C language](/questions/62917/how-to-print-from-parsing-osm-file-with-libxml2-in-c-language)

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
<span id="post-62917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on XML file (in particula .osm file) with libxml2 and C language.</p>
<p>This is my XML source (not all but just a piece):</p>
<pre><code>...
        &lt; way id=&quot;9484424&quot; visible=&quot;true&quot; version=&quot;8&quot; changeset=&quot;11179686&quot; timestamp=&quot;2012-04-04T18:01:31Z&quot; user=&quot;Davlak&quot; uid=&quot;217070&quot;&gt;
      &lt; nd ref=&quot;72843570&quot;/&gt;
      &lt; nd ref=&quot;963203594&quot;/&gt;
      &lt; nd ref=&quot;612588857&quot;/&gt;
      &lt; nd ref=&quot;300164764&quot;/&gt;
      &lt; nd ref=&quot;72843572&quot;/&gt;
      &lt; tag k=&quot;highway&quot; v=&quot;unclassified&quot;/&gt;
      &lt; tag k=&quot;name&quot; v=&quot;Via Giorgio Pitacco&quot;/&gt; 
      &lt; tag k=&quot;odbl&quot; v=&quot;clean&quot;/&gt;
      &lt; tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
     &lt; /way&gt;
     &lt; way id=&quot;11378242&quot; visible=&quot;true&quot; version=&quot;29&quot; changeset=&quot;22876351&quot; timestamp=&quot;2014-06-11T18:00:17Z&quot; user=&quot;Davlak&quot; uid=&quot;217070&quot;&gt;
      &lt; nd ref=&quot;101181728&quot;/&gt;
      &lt; nd ref=&quot;2911704721&quot;/&gt;
      &lt; nd ref=&quot;2911704714&quot;/&gt;
      &lt; nd ref=&quot;101181731&quot;/&gt;
      &lt; tag k=&quot;foot&quot; v=&quot;yes&quot;/&gt;
      &lt; tag k=&quot;highway&quot; v=&quot;trunk_link&quot;/&gt;
      &lt; tag k=&quot;lanes&quot; v=&quot;2&quot;/&gt;
      &lt; tag k=&quot;lit&quot; v=&quot;yes&quot;/&gt;
      &lt; tag k=&quot;maxspeed&quot; v=&quot;40&quot;/&gt;
      &lt; tag k=&quot;mofa&quot; v=&quot;no&quot;/&gt;
      &lt; tag k=&quot;moped&quot; v=&quot;no&quot;/&gt;
      &lt; tag k=&quot;motorroad&quot; v=&quot;yes&quot;/&gt;
      &lt; tag k=&quot;name&quot; v=&quot;Circonvallazione Tiburtina&quot;/&gt;
      &lt; tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
      &lt; tag k=&quot;sidewalk&quot; v=&quot;right&quot;/&gt;
     &lt; /way&gt;
     &lt; way id=&quot;20507982&quot; visible=&quot;true&quot; version=&quot;11&quot; changeset=&quot;17228559&quot; timestamp=&quot;2013-08-05T14:00:29Z&quot; user=&quot;Davlak&quot; uid=&quot;217070&quot;&gt;
      &lt; nd ref=&quot;219557958&quot;/&gt;
      &lt; nd ref=&quot;1920238894&quot;/&gt;
      &lt; nd ref=&quot;1701671630&quot;/&gt;
      &lt; nd ref=&quot;1920238892&quot;/&gt;
      &lt; nd ref=&quot;219557991&quot;/&gt;
      &lt; tag k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
      &lt; tag k=&quot;lit&quot; v=&quot;yes&quot;/&gt;
      &lt; tag k=&quot;name&quot; v=&quot;Via Prenestina&quot;/&gt;
     &lt; /way&gt;
     &lt; way id=&quot;20507983&quot; visible=&quot;true&quot; version=&quot;14&quot; changeset=&quot;26174383&quot; timestamp=&quot;2014-10-18T17:12:55Z&quot; user=&quot;Privits&quot; uid=&quot;2009312&quot;&gt;
      &lt; nd ref=&quot;219558042&quot;/&gt;
      &lt; nd ref=&quot;2276045993&quot;/&gt;
      &lt; nd ref=&quot;2023496104&quot;/&gt;
      &lt; nd ref=&quot;219558031&quot;/&gt;
      &lt; nd ref=&quot;2276045996&quot;/&gt;
      &lt; nd ref=&quot;922740441&quot;/&gt;
      &lt; nd ref=&quot;922740415&quot;/&gt;
      &lt; nd ref=&quot;3137149509&quot;/&gt;
      &lt; nd ref=&quot;1620785409&quot;/&gt;
      &lt; nd ref=&quot;219558021&quot;/&gt;
      &lt; nd ref=&quot;301486927&quot;/&gt;
      &lt; nd ref=&quot;298561544&quot;/&gt;
      &lt; tag k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
      &lt; tag k=&quot;lanes&quot; v=&quot;1&quot;/&gt;
      &lt; tag k=&quot;name&quot; v=&quot;Via Prenestina&quot;/&gt;
      &lt; tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
      &lt; /way&gt;
&#10; ...</code></pre>
<p>My output, right now , is (so using the following code i'm printing):</p>
<pre><code>way: 9484424
 node: 72843570
 node: 963203594
 node: 612588857
 node: 300164764
 node: 72843572</code></pre>
<p>and so on for each way element...</p>
<p>I would like to print, for each way, ONLY the first and the last node, in the same line, and the way that these nodes connect. For example:</p>
<pre><code>node: 72843570 node: 72843572 way: 9484424</code></pre>
<p>This is my code actually:</p>
<hr />
<pre><code>#include &lt;stdio.h&gt;
#include &lt;libxml/parser.h&gt;
#include &lt;libxml/tree.h&gt;
&#10;
int is_leaf(xmlNode * node) {
&#10;    xmlNode * child = node-&gt;children;
&#10;    while(child)  {
&#10;        if(child-&gt;type == XML_ELEMENT_NODE) return 0;
&#10;    child = child-&gt;next;
  }
&#10;  return 1;
}
&#10;void print_xml(xmlNode * node, int indent_len) {
        char *name= &quot;way&quot;;
        char *nd = &quot;nd&quot;;
    while(node)    {
&#10;        if(node-&gt;type == XML_ELEMENT_NODE)  {
            if(strcmp (node-&gt;name, name) ==0)  {
&#10;                printf(&quot;%*c%s: %s\n&quot;, indent_len*2, &#39; &#39;, node-&gt;name, is_leaf(node)?xmlNodeGetContent(node):xmlGetProp(node, &quot;id&quot;));
&#10;            }
&#10;        }
&#10;        if(node-&gt;type == XML_ELEMENT_NODE)  {
            if(strcmp (node-&gt;name, nd) ==0)  {
&#10;                printf(&quot;%*c%s: %s\n&quot;, indent_len*2, &#39; &#39;, &quot;node&quot;, is_leaf(node)?xmlNodeGetContent(node):xmlGetProp(node, &quot;ref&quot;));
&#10;            }
&#10;        }
        print_xml(node-&gt;children, indent_len + 1);
        node = node-&gt;next;
&#10;    }
}
&#10;int main() {
  xmlDoc *doc = NULL;
  xmlNode *root_element = NULL;
&#10;  doc = xmlReadFile(&quot;Casal.osm&quot;, NULL, 0);
&#10;  if (doc == NULL) {
    printf(&quot;Could not parse the XML file&quot;);
  }
&#10;  root_element = xmlDocGetRootElement(doc);
&#10;  print_xml(root_element, 1);
&#10;  xmlFreeDoc(doc);
&#10;  xmlCleanupParser();
}</code></pre>
<p>I'm not able to save or to store the first and last node and print every way during the scan. How can I modify my code? THank you everybody.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-libxml2" rel="tag" title="see questions tagged &#39;libxml2&#39;">libxml2</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-printf" rel="tag" title="see questions tagged &#39;printf&#39;">printf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '18, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/981993fc27750583440927127b4da914?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="claudiodipilla87&#39;s gravatar image" />
<p><span>claudiodipil...</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="claudiodipilla87 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>05 Apr '18, 12:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-62917" class="comments-container">
&#10;</div>
<div id="comment-tools-62917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62917-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question: https://help.openstreetmap.org/questions/62916/parsing-osm-file-with-libxml2-in-c-language" by scai 05 Apr '18, 12:05

</div>

</div>

</div>

