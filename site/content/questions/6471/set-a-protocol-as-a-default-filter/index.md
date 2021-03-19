+++
type = "question"
title = "Set a Protocol as a Default Filter"
description = '''Hello All, I would like to set a protocol as a default display filter forever instead of always writing the protocol name in the Filter combo box whenever I open Wireshark. I&#x27;d like to hard-code it so that it remains forvever as my setting. Kindly, Provide the solution. Thanks, Regards, S.Prashanth.'''
date = "2011-09-20T19:43:00Z"
lastmod = "2011-09-28T00:00:00Z"
weight = 6471
keywords = [ "display-filter" ]
aliases = [ "/questions/6471" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Set a Protocol as a Default Filter](/questions/6471/set-a-protocol-as-a-default-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6471-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I would like to set a protocol as a default display filter forever instead of always writing the protocol name in the Filter combo box whenever I open Wireshark. I'd like to hard-code it so that it remains forvever as my setting. Kindly, Provide the solution.</p><p>Thanks, Regards, S.Prashanth.</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '11, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Sep '11, 06:47</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6471" class="comments-container"></div><div id="comment-tools-6471" class="comment-tools"></div><div class="clear"></div><div id="comment-6471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="6607"></span>

<div id="answer-container-6607" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6607-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks all. I have resolved it by backporting the <code>-d</code> parameter, which initializes the display filter, from Wireshark 1.7.0 to 1.6.1. I also made the display-filter initialization "permanent", such that it always initializes to a specific value. I just changed <code>main.c</code>.</p><pre><code>gchar *dfilter=&quot;http&quot;;

if (dfilter) {
   GtkWidget *filter_te;

   filter_te = gtk_bin_get_child(GTK_BIN(g_object_get_data(G_OBJECT(top_level), E_DFILTER_CM_KEY)));
   gtk_entry_set_text(GTK_ENTRY(filter_te), dfilter);

    /* Run the display filter so it goes in effect. */
    main_filter_packets(&amp;cfile, dfilter, FALSE);
}</code></pre></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '11, 05:24</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6607" class="comments-container"></div><div id="comment-tools-6607" class="comment-tools"></div><div class="clear"></div><div id="comment-6607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6561"></span>

<div id="answer-container-6561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6561-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Find the place where lua scripts should go and create the following 3 files. init.lua must have the same name. Others can be renamed. Last file is where you can customize your default filter.</p><pre><code>init.lua:
-----------------------------------
do
-- load default filter script
dofile(&quot;lua_scripts/default_filter.lua&quot;);
end
-----------------------------------

lua_scripts/default_filter.lua:
-----------------------------------
-- load default filter settings
dofile(&quot;conditions/initfilter.lua&quot;);

do

    -- set default filter
    local function init_defaultFilter()
        local tap = Listener.new(&quot;frame&quot;,&quot;tcp&quot;)
        local initialized = false;

        function tap.reset()
            --set the filter only once
            if( not initialized )
            then
               defaultFilter = defaultFilter or &quot;&quot;;
               set_filter(defaultFilter);
               apply_filter();
               initialized = true;
            end
        end

        -- this function will be called for every packet
        function tap.packet(pinfo,tvb,tapdata)
        end
    end

    -- apply default filter
    init_defaultFilter();
end
-----------------------------------

conditions/initfilter.lua: (my example:)
-----------------------------------
defaultFilter = &quot;sip or http&quot;
-----------------------------------</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '11, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/6fe350be1625b29d7944d6ab430e57ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hiftu&#39;s gravatar image" /><p>Hiftu<br />
<span class="score" title="44 reputation points">44</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hiftu has no accepted answers">0%</span></p></div></div><div id="comments-container-6561" class="comments-container"><span id="6573"></span><div id="comment-6573" class="comment"><div id="post-6573-score" class="comment-score"></div><div class="comment-text"><p>There's a few problems with this solution:</p><p>1) In this case, you don't need <code>init.lua</code> (or even three files...a single file suffices, but "to each his own").</p><p>2) All Lua scripts are loaded <em>automatically</em> if they're in any of the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html"><code>plugins</code></a> directories (or their subdirectories). So, your use of <code>dofile('xyz')</code> while the <code>'xyz'</code> file is under <code>plugins</code> causes the file to be loaded twice. In your example, this creates two taps that do the same thing. Harmless here, but the bug makes this a bad example.</p></div><div id="comment-6573-info" class="comment-info"><span class="comment-age">(26 Sep '11, 19:14)</span> helloworld</div></div><span id="6582"></span><div id="comment-6582" class="comment"><div id="post-6582-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I am a linux user. I had to add init.lua in my system. I like splitting the config and the script so it is easy to modify even with little knowledge in lua scripting.</p></div><div id="comment-6582-info" class="comment-info"><span class="comment-age">(27 Sep '11, 00:41)</span> Hiftu</div></div><span id="6592"></span><div id="comment-6592" class="comment"><div id="post-6592-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Sorry, I am a linux user. I had to add init.lua in my system.</p></blockquote><p>This isn't required in Ubuntu 11.04. Which flavor (and specific version) of Linux are you running?</p></div><div id="comment-6592-info" class="comment-info"><span class="comment-age">(27 Sep '11, 06:43)</span> helloworld</div></div><span id="6593"></span><div id="comment-6593" class="comment"><div id="post-6593-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I like splitting the config and the script so it is easy to modify even with little knowledge in lua scripting.</p></blockquote><p>When the config and script are so short (as in this case), there's little advantage in splitting the files. Even if you wanted to organize your files this way, you should rename the config file extension to something other than <code>.lua</code> in order to prevent Wireshark Lua from auto-loading it in addition to your explicit <code>dofile()</code>. Another way to prevent the auto-load is to move the file outside of the <code>plugins</code> directories.</p></div><div id="comment-6593-info" class="comment-info"><span class="comment-age">(27 Sep '11, 06:43)</span> helloworld</div></div><span id="6595"></span><div id="comment-6595" class="comment"><div id="post-6595-score" class="comment-score"></div><div class="comment-text"><p>Oh, I currently use the ~/.wireshark directory. Where is the plugin directory? (I work in enterprise environment , and I haven't got root access. BTW it is SLED10.)</p></div><div id="comment-6595-info" class="comment-info"><span class="comment-age">(27 Sep '11, 07:25)</span> Hiftu</div></div><span id="6604"></span><div id="comment-6604" class="comment not_top_scorer"><div id="post-6604-score" class="comment-score"></div><div class="comment-text"><p>The <code>plugins</code> directories are listed in the manual (<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html">Table A.1 Configuration files and folders</a>). Your personal plugins (Lua in this case) would be in <strong><code>~/.wireshark/plugins</code></strong> (you might need to create the subdirectory).</p></div><div id="comment-6604-info" class="comment-info"><span class="comment-age">(27 Sep '11, 20:51)</span> helloworld</div></div></div><div id="comment-tools-6561" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-6561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6472"></span>

<div id="answer-container-6472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6472-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't have a way to set a default display filter.</p><p>I suggest filing an enhancement request (or providing a patch to implement this functionality) at bugs.wireshark.org .</p><p>Note that although there is a <code>-R &lt;filter&gt;</code> option when starting Wireshark which will apply the filter when an input file specified with <code>-r</code> is read, this does not set the filter as a default display filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '11, 20:33</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '11, 20:34</p></div></div><div id="comments-container-6472" class="comments-container"><span id="6476"></span><div id="comment-6476" class="comment"><div id="post-6476-score" class="comment-score">1</div><div class="comment-text"><p>I think <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2463">bug 2463</a> already covers this.</p></div><div id="comment-6476-info" class="comment-info"><span class="comment-age">(21 Sep '11, 05:49)</span> cmaynard ♦♦</div></div><span id="6572"></span><div id="comment-6572" class="comment"><div id="post-6572-score" class="comment-score">1</div><div class="comment-text"><p>An update: Thanks to <a href="http://wiki.wireshark.org/StigBj%C3%B8rlykke">Stig</a>, as of <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=39090">r39090</a>, which closes <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2463">bug 2463</a>, Wireshark now takes a <code>-d &lt;display_filter&gt;</code> command-line option to set the active display filter when Wireshark starts. Until 1.7.0 is released, you can download and try any <a href="http://www.wireshark.org/download/automated/">automated</a> installer that is version 39090 or later.</p></div><div id="comment-6572-info" class="comment-info"><span class="comment-age">(26 Sep '11, 18:24)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-6472" class="comment-tools"></div><div class="clear"></div><div id="comment-6472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

