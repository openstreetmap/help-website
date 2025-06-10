+++
type = "question"
title = "nominatim 4.1.0 initial data import failing on full planet"
description = '''Hi, I am having nominatim 4.1.0 crash multiple times while trying to do the initial import. Any help would be greatly appreciated. I am importing into an Azure VM, machine type Standard E8bs v5 (8 vcpus, 64 GiB memory), disk Premium SSD LRS 2048GiB, OS ubuntu 22.04. I have tried importing the latest...'''
date = "2022-11-13T01:57:00Z"
lastmod = "2022-11-13T21:04:00Z"
weight = 86139
keywords = [ "import", "nominatim", "crash", "osm2pgsql" ]
aliases = [ "/questions/86139" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [nominatim 4.1.0 initial data import failing on full planet](/questions/86139/nominatim-410-initial-data-import-failing-on-full-planet)

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
<span id="post-86139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am having nominatim 4.1.0 crash multiple times while trying to do the initial import. Any help would be greatly appreciated.</p>
<p>I am importing into an Azure VM, machine type Standard E8bs v5 (8 vcpus, 64 GiB memory), disk Premium SSD LRS 2048GiB, OS ubuntu 22.04. I have tried importing the latest planet export which is located at <a href="https://planet.openstreetmap.org/pbf/planet-221107.osm.pbf,">https://planet.openstreetmap.org/pbf/planet-221107.osm.pbf,</a> as well as <a href="https://planet.openstreetmap.org/pbf/planet-221031.osm.pbf">https://planet.openstreetmap.org/pbf/planet-221031.osm.pbf</a> extract to try to rule out data related issues.</p>
<p>I have included the scripts to the full import log as well as the full script to setup Ubuntu at the end of this message.</p>
<p>The import consistently gets to the same number of Nodes and then an error is thrown and I can't continue. I've tried to delete the database and rerun the import. I've also tried to rebuild the machine, and as previously mentioned, also import a different osm extract. The error stack that is thrown is:</p>
<p>Processing: Node(5013370k 550.7k/s) Way(0k 0.00k/s) Relation(0 0.0/s)Traceback (most recent call last):</p>
<pre><code>File &quot;/usr/local/bin/nominatim&quot;, line 14, in &lt;module&gt;
exit(cli.nominatim(module_dir=&#39;/usr/local/lib/nominatim/module&#39;, File &quot;/usr/local/lib/nominatim/lib-python/nominatim/cli.py&quot;, line 264, in nominatim
return parser.run(**kwargs)   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/cli.py&quot;, line 126, in run
return args.command.run(args)   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/clicmd/setup.py&quot;, line 92, in run
database_import.import_osm_data(files, File &quot;/usr/local/lib/nominatim/lib-python/nominatim/tools/database_import.py&quot;, line 108, in import_osm_data
run_osm2pgsql(options)   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/tools/exec_utils.py&quot;, line 152, in run_osm2pgsql
subprocess.run(cmd, cwd=options.get(&#39;cwd&#39;, &#39;.&#39;),   File &quot;/usr/lib/python3.10/subprocess.py&quot;, line 524, in run
raise CalledProcessError(retcode, process.args, subprocess.CalledProcessError: Command &#39;[&#39;/usr/local/lib/nominatim/osm2pgsql&#39;, &#39;--hstore&#39;, &#39;--latlon&#39;, &#39;--slim&#39;, &#39;--with-forward-dependencies&#39;, &#39;false&#39;, &#39;--log-progress&#39;, &#39;true&#39;, &#39;--number-processes&#39;, &#39;1&#39;, &#39;--cache&#39;, &#39;94513&#39;, &#39;--output&#39;, &#39;gazetteer&#39;, &#39;--style&#39;, &#39;/usr/local/etc/nominatim/import-extratags.style&#39;, &#39;--create&#39;, &#39;/var/osm/extract/import.pbf&#39;]&#39; died with &lt;Signals.SIGKILL: 9&gt;.</code></pre>
<p>The command I use to do the initial import is</p>
<p>nominatim import --osm2pgsql-cache 0 --osm-file /var/osm/extract/import.pbf --verbose 2&gt;&amp;1 | tee setup.log</p>
<p>The full setup.log</p>
<p>2022-11-12 22:08:52: Using project directory: /srv/nominatim/nominatim-planet 2022-11-12 22:08:54: Creating database 2022-11-12 22:08:54: Setting up country tables SET SET SET SET SET SET SET SET SET CREATE TABLE COPY 23217 CREATE INDEX 2022-11-12 22:08:55: Importing OSM data file 2022-11-12 22:08:55 osm2pgsql version 1.6.0 2022-11-12 22:08:55 Database version: 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1) 2022-11-12 22:08:55 PostGIS version: 3.2 2022-11-12 22:08:55 Parsing gazetteer style file '/usr/local/etc/nominatim/import-extratags.style'. NOTICE: table "place" does not exist, skipping Processing: Node(5013370k 550.7k/s) Way(0k 0.00k/s) Relation(0 0.0/s)Traceback (most recent call last): File "/usr/local/bin/nominatim", line 14, in &lt;module&gt; exit(cli.nominatim(module_dir='/usr/local/lib/nominatim/module', File "/usr/local/lib/nominatim/lib-python/nominatim/cli.py", line 264, in nominatim return parser.run(**kwargs) File "/usr/local/lib/nominatim/lib-python/nominatim/cli.py", line 126, in run return args.command.run(args) File "/usr/local/lib/nominatim/lib-python/nominatim/clicmd/setup.py", line 92, in run database_import.import_osm_data(files, File "/usr/local/lib/nominatim/lib-python/nominatim/tools/database_import.py", line 108, in import_osm_data run_osm2pgsql(options) File "/usr/local/lib/nominatim/lib-python/nominatim/tools/exec_utils.py", line 152, in run_osm2pgsql subprocess.run(cmd, cwd=options.get('cwd', '.'), File "/usr/lib/python3.10/subprocess.py", line 524, in run raise CalledProcessError(retcode, process.args, subprocess.CalledProcessError: Command '['/usr/local/lib/nominatim/osm2pgsql', '--hstore', '--latlon', '--slim', '--with-forward-dependencies', 'false', '--log-progress', 'true', '--number-processes', '1', '--cache', '94513', '--output', 'gazetteer', '--style', '/usr/local/etc/nominatim/import-extratags.style', '--create', '/var/osm/extract/import.pbf']' died with &lt;signals.sigkill: 9=""&gt;.</p>
<p>Ubuntu Setup Steps</p>
<p>sudo mkdir -p /var/osm/extract sudo chmod 777 /var/osm/extract</p>
<p>#planet</p>
<p>wget -P /var/osm/extract <a href="https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf">https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf</a> mv /var/osm/extract/planet-latest.osm.pbf /var/osm/extract/import.pbf</p>
<p>sudo useradd -d /srv/nominatim -s /bin/bash -m nominatim su nominatim</p>
<p>sudo apt-get update -qq sudo apt install -y php-cgi sudo apt install -y build-essential cmake g++ libboost-dev libboost-system-dev \ libboost-filesystem-dev libexpat1-dev zlib1g-dev \ libbz2-dev libpq-dev \ postgresql-server-dev-14 postgresql-14-postgis-3 \ postgresql-contrib-14 postgresql-14-postgis-3-scripts \ php-cli php-pgsql php-intl libicu-dev python3-dotenv \ python3-psycopg2 python3-psutil python3-jinja2 \ python3-icu python3-datrie</p>
<p>export USERNAME=nominatim export USERHOME=/srv/nominatim</p>
<p>chmod a+x $USERHOME</p>
<p>sudo sed -i 's/#listen_addresses = '\''localhost'\''/listen_addresses = '\''*'\''/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/shared_buffers = 128MB/shared_buffers = 2GB/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#maintenance_work_mem = 64MB/maintenance_work_mem = 10GB/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#autovacuum_work_mem = -1/autovacuum_work_mem = 2GB/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#work_mem = 4MB/work_mem = 50MB/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#effective_cache_size = 4GB/effective_cache_size = 24GB/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#synchronous_commit = on/synchronous_commit = off/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#checkpoint_timeout = 5min/checkpoint_timeout = 10min/g' /etc/postgresql/14/main/postgresql.conf sudo sed -i 's/#checkpoint_completion_target = 0.5/checkpoint_completion_target = 0.9/g' /etc/postgresql/14/main/postgresql.conf</p>
<p>echo '# Allow remote connections, the firewall limits external requests' | sudo tee /etc/postgresql/14/main/pg_hba.conf -a echo 'host all all 0.0.0.0/0 md5' | sudo tee /etc/postgresql/14/main/pg_hba.conf -a</p>
<p>sudo systemctl restart postgresql</p>
<p>sudo -u postgres createuser -s $USERNAME sudo -u postgres createuser www-data</p>
<p>cd $USERHOME wget <a href="https://nominatim.org/release/Nominatim-4.1.0.tar.bz2">https://nominatim.org/release/Nominatim-4.1.0.tar.bz2</a> tar xf Nominatim-4.1.0.tar.bz2 cd Nominatim-4.1.0</p>
<p>wget -O data/country_osm_grid.sql.gz <a href="https://www.nominatim.org/data/country_grid.sql.gz">https://www.nominatim.org/data/country_grid.sql.gz</a></p>
<p>mkdir build cd build cmake .. make sudo make install</p>
<p>mkdir $USERHOME/nominatim-project cd $USERHOME/nominatim-project</p>
<p>sudo apt install -y apache2 libapache2-mod-php</p>
<p>sudo tee /etc/apache2/conf-available/nominatim.conf &lt;&lt; EOFAPACHECONF &lt;directory "$userhome="" nominatim-project="" website"=""&gt; Options FollowSymLinks MultiViews AddType text/html .php DirectoryIndex search.php Require all granted &lt;/directory&gt;</p>
<p>Alias /nominatim $USERHOME/nominatim-project/website EOFAPACHECONF</p>
<p>sudo a2enconf nominatim sudo systemctl restart apache2</p>
<p>mkdir ~/nominatim-planet cd ~/nominatim-planet</p>
<p>export PROJECT_DIR=~/nominatim-planet</p>
<p>sudo mkdir -p /var/osm/cache sudo chmod 777 /var/osm/cache</p>
<p>wget <a href="https://www.nominatim.org/data/wikimedia-importance.sql.gz">https://www.nominatim.org/data/wikimedia-importance.sql.gz</a> wget <a href="https://www.nominatim.org/data/gb_postcodes.csv.gz">https://www.nominatim.org/data/gb_postcodes.csv.gz</a> wget <a href="https://www.nominatim.org/data/us_postcodes.csv.gz">https://www.nominatim.org/data/us_postcodes.csv.gz</a></p>
<p>cp ~/Nominatim-4.1.0/settings/env.defaults . sudo sed -i 's/NOMINATIM_FLATNODE_FILE=/NOMINATIM_FLATNODE_FILE=\/var\/osm\/cache\/flatnode.file/g' env.defaults</p>
<p>nominatim import --osm2pgsql-cache 0 --osm-file /var/osm/extract/import.pbf --verbose 2&gt;&amp;1 | tee setup.log</p>
<p>Any help is really appreciated!</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '22, 01:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d554c07eb8422e11c3e28d841c078122?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SuperUniqueName&#39;s gravatar image" />
<p><span>SuperUniqueName</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SuperUniqueName has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86139" class="comments-container">
&#10;</div>
<div id="comment-tools-86139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86139-form-container" class="comment-form-container">
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

<span id="86142"></span>

<div id="answer-container-86142" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86142-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SuperUniqueName has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You use the wrong name for your configuration file. The name should be <code>.env</code>. Therefore the flatnode configuration is not picked up by Nominatim and it runs out of memory.</p>
<p>Other things to consider:</p>
<ul>
<li>Don't copy the full default config file. Simply put a <code>.env</code> file in place which contains only the settings you want to change.</li>
<li>Don't use the option <code>--osm2pgsql-cache</code>. Nominatim will do the right thing per default. (And apparently not the right thing when <code>--osm2pgsql-cache 0</code> is given. There is a bug there that needs fixing.)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '22, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-86142" class="comments-container">
<span id="86146"></span>
<div id="comment-86146" class="comment">
<div id="post-86146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Ionvia,</p>
<p>Thanks so much for taking the time to read my issue and share your reply. I can see now that the flatfile was not being created, which heavily points to the fact that the configure file was not being read and points to your solution.</p>
<p>I've changed my script from</p>
<p>cp ~/Nominatim-4.1.0/settings/env.defaults . sudo sed -i 's/NOMINATIM_FLATNODE_FILE=/NOMINATIM_FLATNODE_FILE=\/var\/osm\/cache\/flatnode.file/g' env.defaults</p>
<p>to be</p>
<p>echo 'NOMINATIM_FLATNODE_FILE=/var/osm/cache/flatnode.file' | tee .env -a</p>
<p>and have re-run the script.</p>
<p>Not sure where to put improvement ideas for Nominatim but it'd be great if in nominatim import --verbose mode, it output the values of the configuration variables that it's running with e.g. NOMINATIM_DATABASE_DSN="pgsql:dbname=nominatim" NOMINATIM_DATABASE_WEBUSER="www-data" ... NOMINATIM_FLATNODE_FILE= or NOMINATIM_FLATNODE_FILE=/var/osm/cache/flatnode.file</p>
<p>as I found it really hard to get visibility over the configuration settings that nominatim was running with.</p>
<p>Alternatively it could had some text to say "Running using configuration file /user/nominatim/nominatim_planet/.env" or "Running with no custom configuration file"</p>
<p>Aside from that, just another huge thanks Ionvia!</p>
<p>Cheers,</p>
</div>
<div id="comment-86146-info" class="comment-info">
<span class="comment-age">(13 Nov '22, 21:04)</span> <span class="comment-user userinfo">SuperUniqueName</span>
</div>
</div>
</div>
<div id="comment-tools-86142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86142-form-container" class="comment-form-container">
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

