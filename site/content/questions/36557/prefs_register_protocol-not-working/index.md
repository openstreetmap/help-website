+++
type = "question"
title = "prefs_register_protocol not working.."
description = '''Hi all, I am a beginner in wireshark plugin development so..i have been going through the docs trying to compile a plugin(dissector)which just captures UDP packets at some fixed port and displays as mydisc protocol which seems to work.Now i am trying to add this protocol in the list of protocols wit...'''
date = "2014-09-24T01:49:00Z"
lastmod = "2015-02-04T02:08:00Z"
weight = 36557
keywords = [ "customprotocols", "preferences", "protocols" ]
aliases = [ "/questions/36557" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [prefs\_register\_protocol not working..](/questions/36557/prefs_register_protocol-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36557-score" class="post-score" title="current number of votes">0</div><span id="post-36557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am a beginner in wireshark plugin development so..i have been going through the docs trying to compile a plugin(dissector)which just captures UDP packets at some fixed port and displays as mydisc protocol which seems to work.Now i am trying to add this protocol in the list of protocols with options in preferences tab in edit,so that i can give some port rather than having a fixed udp port.here is the code.</p><pre><code>#include &quot;config.h&quot;
#include &lt;string.h&gt;
#include &lt;glib.h&gt;
#include &lt;epan/packet.h&gt;
#define MYDISC_PORT 3001
static int proto_mydisc = -1;
static gboolean flag = TRUE;
static void dissect_mydisc(tvbuff_t *tvb ,packet_info *pinfo ,proto_tree *tree)
{
 col_set_str(pinfo-&gt;cinfo,COL_PROTOCOL,&quot;MYDISC&quot;);
 col_clear(pinfo-&gt;cinfo,COL_INFO);

}
void proto_register_mydisc(void)
{
module_t* mydisc_module;
prefs_set_pref(&quot;udp.try_heuristic_first:true&quot;);
proto_mydisc = proto_register_protocol(

&quot;mydisc protocol&quot;,
&quot;Mydisc&quot;,
&quot;mydisc&quot;
);
mydisc_module = prefs_register_protocol(proto_mydisc,NULL);
prefs_register_bool_preference(mydisc_module ,&quot;flag&quot;,&quot;flag&quot;,&quot;flag&quot;,&amp;flag);
}
void proto_reg_handoff_mydisc(void)
{
static dissector_handle_t mydisc_handle;
mydisc_handle = create_dissector_handle(dissect_mydisc,proto_mydisc);
dissector_add_uint(&quot;udp.port&quot;,MYDISC_PORT,mydisc_handle);
}</code></pre><p>After compiling the plugin and adding its the so files in libs i restart my wireshark but i cant find mydisc protocol in edit-&gt;preferences-&gt;protocols.Please help!! thnx in advance!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-customprotocols" rel="tag" title="see questions tagged &#39;customprotocols&#39;">customprotocols</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-protocols" rel="tag" title="see questions tagged &#39;protocols&#39;">protocols</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p><span>koundi</span><br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '14, 01:58</strong> </span></p></div></div><div id="comments-container-36557" class="comments-container"></div><div id="comment-tools-36557" class="comment-tools"></div><div class="clear"></div><div id="comment-36557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36560"></span>

<div id="answer-container-36560" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36560-score" class="post-score" title="current number of votes">1</div><span id="post-36560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="koundi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure your dissector is being loaded in the first place? A simple way to tell would be to enter "mydisc" in the display filter bar. If it turns green then your dissector is loaded, else not.</p><p>I'm guessing your dissector is not being loaded at all.</p><p>Are you building this dissector as a built-in dissector or as a plugin (is it in epan/dissectors/ or in plugins/mydisc/ or similar)? It's a lot easier to build it as a built-in dissector: all you have to do is modify epan/dissectors/Makefile.common (or epan/dissectors/Custom.common if you don't plan to submit the file to Wireshark) and then rebuild libwireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '14, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36560" class="comments-container"><span id="36576"></span><div id="comment-36576" class="comment"><div id="post-36576-score" class="comment-score">1</div><div class="comment-text"><p>You can also see what plugins are loaded in the "About..." dialog in the "Plugins" tab; do Help &gt; About in the GTK+ version and non-OS X Qt versions or Wireshark &gt; About in the OS X Qt version.</p></div><div id="comment-36576-info" class="comment-info"><span class="comment-age">(24 Sep '14, 17:08)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="39468"></span><div id="comment-39468" class="comment"><div id="post-39468-score" class="comment-score"></div><div class="comment-text"><p>thanks so much for replying...I know its late but ya i figured things out and did not bother to look back at this one!!And yes i was trying to build a plugin not a built -in dissector which i now know is the easier way :)</p></div><div id="comment-39468-info" class="comment-info"><span class="comment-age">(29 Jan '15, 00:49)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="39469"></span><div id="comment-39469" class="comment"><div id="post-39469-score" class="comment-score"></div><div class="comment-text"><p>Also when i build a plugin the .so files(from /plugins/mydisc/.libs) of the plugin are not copied immediately into local /.wireshark folder i had to do it manually and it was not mentioned in the Readme for plugins...maybe you guys can look into it!!Thanks!!</p></div><div id="comment-39469-info" class="comment-info"><span class="comment-age">(29 Jan '15, 00:52)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="39488"></span><div id="comment-39488" class="comment"><div id="post-39488-score" class="comment-score"></div><div class="comment-text"><p>The README.plugins file says</p><blockquote><p>The bad news is that Wireshark will not use the plugins unless the plugins are installed in one of the places it expects them to find.</p></blockquote><p>although the subsequent suggestions could use more work - and there should also be a discussion about Windows.</p><p>That document is somewhat oriented towards building a version of Wireshark bundled with the new plugin, rather than to building personal plugins; it sounds as if you're building a personal plugin. The plugins should <em>not</em> be automatically copied into your personal plugin folder, as that would be inappropriate when building a version of Wireshark with bundled plugins. The document should be expanded to both cover Windows and cover the "building a personal plugin" case.</p><p>(And, in the longer term, adding the ability to describe protocols with purely declarative text files, such as <a href="http://wsgd.free.fr">Wireshark Generic Dissector</a> files, or ASN.1/various DCE IDLs/rpcgen/xcb/CORBA IDL/etc. with conformance files, without requiring any compilation, would <em>really</em> help; you can already write dissectors in Lua and use them in versions of Wireshark that include embedded Lua, without needing to do any compilation.)</p></div><div id="comment-39488-info" class="comment-info"><span class="comment-age">(29 Jan '15, 13:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="39629"></span><div id="comment-39629" class="comment"><div id="post-39629-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for replying, I guess that does make sense but the only point i was trying to make was that after changing personal plugin details in the config file and other files as specified in the Readme.plugins and then using make command should mean that the user is trying to make the build with his own plugin bundled with wireshark. So making him manually transfer files from ./libs folder to one of the places wireshark expects them to be present imho is unnecessary.</p></div><div id="comment-39629-info" class="comment-info"><span class="comment-age">(04 Feb '15, 02:08)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-36560" class="comment-tools"></div><div class="clear"></div><div id="comment-36560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

